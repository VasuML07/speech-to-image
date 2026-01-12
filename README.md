# 📝 Text to Image (Offline & Free)

This project converts user-entered text into an image and allows
downloading the output as a PNG or PDF.

The application is built using Streamlit and runs fully offline.

---

## 🚀 Features
- Text input (up to 400 characters)
- Local image generation
- Download as PNG or PDF
- Clean and interactive Streamlit UI
- No API keys required

---

## 🧠 Tech Stack
- Python
- Streamlit
- Pillow
- Requests

---

## ▶️ How to Run Locally

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run speechtoimage.py
y

## 📁 Project Structure
PRO/
├── speechtoimage.py
├── requirements.txt
├── .gitignore
├── venv/
└── vosk-model/