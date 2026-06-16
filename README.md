# 🤖 Jarvis — AI Voice Assistant

A lightweight voice assistant powered by **Google Gemini AI**. Just say *"Jarvis"* and ask anything — it listens, thinks, and talks back.

---

## ✨ Features

- 🎙️ **Wake word activation** — always listening for "Jarvis"
- 🗣️ **Natural voice responses** — powered by Google Text-to-Speech
- 🧠 **Gemini 2.5 Flash** — fast, accurate AI responses
- 🔒 **Secure** — API key stored in `.env`, never hardcoded

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/pa1nagar/Jarvis.git
cd Jarvis
```

### 2. Create a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your API key

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

Get your free API key at [aistudio.google.com](https://aistudio.google.com/app/apikey)

### 5. Run it

```bash
python main.py
```

---

## 🗂️ Project Structure

```
Jarvis/
├── main.py          # Core assistant logic
├── requirements.txt # Dependencies
├── .env             # API key (not committed)
└── .gitignore
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| `speech_recognition` | Captures voice input via microphone |
| `gTTS` | Converts text responses to speech |
| `pygame.mixer` | Plays audio responses |
| `google-genai` | Gemini AI for understanding and responding |
| `python-dotenv` | Loads API key from `.env` securely |

---

## 📋 Requirements

- Python 3.9+
- A working microphone
- Internet connection
- Gemini API key (free at [aistudio.google.com](https://aistudio.google.com))

---

## 💡 Usage

1. Run the assistant
2. Wait for `"Initializing Jarvis..."`
3. Say **"Jarvis"** out loud
4. It replies **"Ya"** — now ask your question
5. Jarvis responds with voice

---

## 🔮 Planned Features

- [ ] Conversation memory across sessions
- [ ] Weather & calendar integration
- [ ] System controls (volume, apps)
- [ ] GUI dashboard

---

## 📄 License

MIT License — free to use and modify.
