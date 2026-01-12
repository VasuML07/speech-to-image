🎤 Speech to Image Generator (Offline & Free)

A Streamlit-based offline application that converts spoken audio into text using the Vosk speech recognition model and then generates an image containing the recognized text.

The output can be downloaded as PNG or PDF.

This project is fully offline, API-free, and reproducible, making it ideal for learning, demonstrations, and academic projects where internet access or cloud APIs are restricted.

🚀 Why This Project Is Different

Unlike popular AI tools such as ChatGPT or Gemini, which rely on cloud APIs and continuous internet connectivity, this project focuses on:

✅ Fully offline execution

✅ No API keys or paid services

✅ Complete control over data and outputs

✅ Transparent and explainable processing pipeline

✅ Local execution suitable for restricted environments

This makes the project especially valuable for education, labs, and institutions where cloud-based AI tools are unavailable or restricted.

✨ Features

🎙️ Record voice input (up to 10 seconds)

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

User can download the output as PNG or PDF

All processing happens locally on the user’s machine, ensuring predictability, privacy, and reproducibility.

🆚 Comparison with Cloud AI Tools
Feature	This Project	ChatGPT / Gemini
Offline usage	✅ Yes	❌ No
Internet required	❌ No	✅ Yes
API key needed	❌ No	✅ Yes
Usage limits	❌ No	✅ Yes
Direct image/PDF download	✅ Yes	❌ Limited
Full code control	✅ Yes	❌ No
Reproducible output	✅ Yes	❌ No

This project does not aim to replace cloud AI models.
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


Large files such as virtual environments, audio recordings, and Vosk models are intentionally excluded from version control.

▶️ How to Run on Your Computer (Local Setup)
1️⃣ Clone the repository
git clone https://github.com/your-username/speech-to-image.git
cd speech-to-image

2️⃣ Create and activate a virtual environment

Windows

python -m venv venv
venv\Scripts\activate


Linux / macOS

python3 -m venv venv
source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Download the Vosk model

Download an English Vosk model from the official site:

👉 https://alphacephei.com/vosk/models

Recommended:

vosk-model-small-en-us-0.15


Extract and place it inside the project directory as:

speech-to-image/
├── vosk-model/
│   ├── am
│   ├── conf
│   └── ...

5️⃣ Run the application
streamlit run speechtoimage.py

6️⃣ Open in browser
http://localhost:8501


Make sure your microphone is connected and allowed.

☁️ Deployment Notes

This application cannot be deployed on Streamlit Cloud due to:

Microphone access limitations

Local Vosk model requirements

A text-only version (without live audio recording) can be deployed separately for cloud demonstration.

The full speech-based pipeline is intentionally local by design.

🎯 Use Cases

College mini or major projects

Offline AI demonstrations

Speech processing learning

Python + Streamlit practice

Portfolio project showcasing system design and offline-first architecture

⚠️ Important Notes

Microphone access is required

Vosk models must be downloaded separately

Generated files are excluded using .gitignore

This project focuses on speech-to-text and visualization, not AI image generation

📌 Future Enhancements

Improved text wrapping and layout handling

Adjustable font sizes and themes

Multi-language speech support

Integration with local image-generation models (e.g., Stable Diffusion)

History and gallery view for generated images

👨‍💻 Author

Developed as a lightweight, offline, and transparent alternative to cloud-dependent AI tools, with a strong focus on learning, reproducibility, and responsible system design.

✅ Summary

This project demonstrates:

Practical software engineering

Offline-first system architecture

Clean UI development with Streamlit

Honest and realistic project scoping

Clear differentiation from cloud-based AI platforms

If you want next:

I can tighten this further for recruiters

Add architecture diagram

Or rewrite it in IEEE / academic project format

This README is already internship-grade.
