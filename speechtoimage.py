# ESSENTIAL LIBRARIES

# it helps us for making a simple web app
import streamlit as st

# it lets python download things from internet
import requests

# it lets python use my microphone to record sound
import sounddevice as sd

# this lets us to record sound as .wav file
# wav files are audio files and they store uncompressed sound
import wavio

# helps python to talk to os system
import os

# helps us to store environment variables securely
from dotenv import load_dotenv

# offline speech-to-text model
from vosk import Model, KaldiRecognizer

import json
import wave

# image creation utilities
from PIL import Image, ImageDraw, ImageFont


# load environment variables (no API used, safe to keep)
load_dotenv()


# AUDIO RECORDING FUNCTION
def record_audio(filename, duration, fs):
    print("Recording.....")

    # this records sound from microphone
    # duration * fs tells about total number of sound samples
    # samplerate = fs tells how clear sound is
    recording = sd.rec(
        int(duration * fs),
        samplerate=fs,
        channels=1,
        dtype="int16"
    )

    # tells python to wait until recording is finished
    sd.wait()

    # save the recorded sound into .wav file
    wavio.write(filename, recording, fs, sampwidth=2)

    print("Recording saved as", filename)


# STREAMLIT USER INTERFACE

st.set_page_config(page_title="Speech to Image", layout="centered")

st.title("🎤 Speech to Image (Offline & Free)")
st.caption("Speak → Convert to text → Generate image → Download")

st.sidebar.header("ℹ️ Instructions")
st.sidebar.write(
    """
    • Click the button and speak clearly  
    • Recording duration: **10 seconds**  
    • Works completely **offline**  
    • Output can be downloaded as **PNG or PDF**
    """
)

# used to display text in interface
st.write("Speak here")


# BUTTON
if st.button("🎙️ Click here to speak"):
    with st.spinner("Listening for 10 seconds and generating image..."):

        # audio configuration
        audio_filename = "input.wav"
        duration = 10
        fs = 44100

        # record audio
        record_audio(audio_filename, duration, fs)

        # open audio file
        wf = wave.open(audio_filename, "rb")

        # load vosk model (folder must exist locally)
        model = Model("vosk-model")
        recognizer = KaldiRecognizer(model, wf.getframerate())
        recognizer.SetWords(True)

        text_output = ""

        # speech recognition loop
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                text_output += result.get("text", "") + " "

        final_result = json.loads(recognizer.FinalResult())
        text_output += final_result.get("text", "")

        # clean recognized text
        a = " ".join(text_output.strip().split())

        # display recognized text
        st.success("Recognized Text:")
        st.markdown(f"**{a if a else 'No clear speech detected'}**")

        # IMAGE GENERATION

        image_path = "generated_image.png"
        pdf_path = "generated_image.pdf"

        img = Image.new("RGB", (1024, 1024), color="#f5f5f5")
        draw = ImageDraw.Draw(img)

        text = a if a else "Image Generated"

        try:
            font = ImageFont.truetype("arial.ttf", 60)
        except:
            font = ImageFont.load_default()

        # center text
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        x = (1024 - text_width) // 2
        y = (1024 - text_height) // 2

        draw.text((x, y), text, fill="black", font=font)

        # save outputs
        img.save(image_path)
        img.save(pdf_path, "PDF")

        # show image
        st.image(image_path, caption="Generated Image")

        # download buttons
        col1, col2 = st.columns(2)

        with col1:
            with open(image_path, "rb") as f:
                st.download_button(
                    label="⬇️ Download Image (PNG)",
                    data=f,
                    file_name="speech_image.png",
                    mime="image/png"
                )

        with col2:
            with open(pdf_path, "rb") as f:
                st.download_button(
                    label="⬇️ Download Image (PDF)",
                    data=f,
                    file_name="speech_image.pdf",
                    mime="application/pdf"
                )
