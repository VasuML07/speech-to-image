🎤 Speech to Image Generator (Offline & Free)

A Streamlit-based offline application that converts spoken audio into text using the Vosk speech recognition model and then generates a visual image from the recognized text.
The output can be downloaded as PNG or PDF.

This project is fully offline, API-free, and reproducible, making it ideal for learning, demonstrations, and academic projects.

🚀 Why This Project Is Different

Unlike popular AI tools such as ChatGPT or Gemini, which rely on cloud APIs and internet connectivity, this project focuses on:

✅ Offline execution

✅ No API keys or paid services

✅ Complete control over data and outputs

✅ Transparent, explainable processing pipeline

✅ Local execution suitable for restricted environments

This makes the project especially valuable for education, labs, and institutions where cloud AI tools are unavailable or restricted.

✨ Features

🎙️ Record voice input (10 seconds)

🧠 Offline speech-to-text using Vosk

🖼️ Convert recognized text into an image

📥 Download output as PNG or PDF

⚡ Lightweight and fast

🌐 Interactive Streamlit interface

🔒 No internet or external APIs required

🧠 How It Works

User records voice input through the microphone

Audio is converted to text using the Vosk offline speech recognition model

The recognized text is rendered onto a fixed-size image canvas

The generated image is displayed instantly

User can download the result as PNG or PDF

All processing happens locally on the user’s machine, ensuring predictability and privacy.

🆚 Comparison with Cloud AI Tools
Feature	This Project	ChatGPT / Gemini
Offline usage	✅ Yes	❌ No
Internet required	❌ No	✅ Yes
API key needed	❌ No	✅ Yes
Usage limits	❌ No	✅ Yes
Direct image/PDF download	✅ Yes	❌ Limited
Full code control	✅ Yes	❌ No
Reproducible output	✅ Yes	❌ No

This project does not aim to replace AI models.
Instead, it provides a controlled, offline alternative for speech-based text visualization.

🛠️ Tech Stack

Python

Streamlit – Web interface

Vosk – Offline speech recognition

SoundDevice & Wavio – Audio recording

Pillow (PIL) – Image and PDF generation

📁 Project Structure
speech-to-image/
├── speechtoimage.py
├── requirements.txt
├── README.md
└── .gitignore


Large files such as virtual environments, audio files, and speech models are intentionally excluded from version control.

▶️ Run Locally
1️⃣ Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Download Vosk model

Download a Vosk English model and place it in the project directory as:

vosk-model/

4️⃣ Run the application
streamlit run speechtoimage.py


Open in browser:

http://localhost:8501

☁️ Deployment Notes

This application cannot be deployed on Streamlit Cloud due to microphone and local model restrictions.

A text-only version can be deployed separately for cloud demonstration.

The full speech-based pipeline runs locally by design.

🎯 Use Cases

College mini or major projects

Offline AI demonstrations

Speech processing learning

Python + Streamlit practice

Portfolio project showcasing system design

⚠️ Important Notes

Microphone access is required

Vosk models must be downloaded separately

Generated files are excluded using .gitignore

The project focuses on speech-to-text and visualization, not AI image generation

📌 Future Enhancements

Text wrapping and layout improvements

Adjustable font size and themes

Multi-language speech support

Integration with local AI image models (e.g., Stable Diffusion)

History and gallery view

👨‍💻 Author

Developed as a lightweight, offline, and transparent alternative to cloud-dependent AI tools, with a focus on learning and reproducibility.

✅ Summary

This project demonstrates:

Practical software engineering

Offline-first system design

Clean UI development with Streamlit

Responsible and realistic project scoping

Clear differentiation from cloud-based AI platforms
