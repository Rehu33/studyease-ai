
# 📚 StudyEase AI

StudyEase AI is a simple AI-powered study assistant that transforms long study notes into useful revision materials using a locally running language model.

## ✨ Features

- 📝 Generate short summaries from study notes
- 📌 Extract key revision points
- ❓ Generate practice questions
- 🤖 Powered by Gemma 3 1B through Ollama
- 💻 Runs locally on your computer

## 🛠️ Technologies Used

- Python
- Streamlit
- Ollama
- Gemma 3 1B
- Requests

## ⚙️ Requirements

- Python installed on your computer
- Ollama installed and running
- Git (for cloning the repository)

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Rehu33/studyease-ai.git
cd studyease-ai
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Download the model

```bash
ollama pull gemma3:1b
```

Make sure Ollama is running before starting the app.

### 5. Run StudyEase AI

```bash
streamlit run app.py
```

The app will open in your browser.

## 📖 How to Use

1. Paste your study notes into the text area.
2. Choose one of the available tasks:
   - Short summary
   - Key revision points
   - Practice questions
3. Click **Generate**.
4. Review the generated study material.

## ⚠️ Disclaimer

AI-generated content may contain mistakes. Always verify important information against your original study notes.

## 👩‍💻 Author

**Rehab Alamgir**

GitHub: [@Rehu33](https://github.com/Rehu33)

## 📄 License

This project is open source. A license will be added separately.
