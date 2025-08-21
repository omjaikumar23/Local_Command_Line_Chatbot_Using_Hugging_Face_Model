# 🤖 Local Command-Line Chatbot Using Hugging Face

Welcome to the Local Command-Line Chatbot project! This chatbot leverages the Hugging Face `facebook/blenderbot-400M-distill` text generation model to deliver coherent multi-turn conversations by maintaining a short-term memory of recent exchanges.

---

## 🚀 Project Overview

This project aims to build a fully functional, local chatbot interface using a Hugging Face text generation model. It runs entirely on your machine (GPU optional) and ensures smooth, interactive conversations via a command-line interface (CLI), managing context with a sliding window memory buffer.

---

## ✨ Key Features

- Utilizes the Hugging Face `facebook/blenderbot-400M-distill` model with the `text2text-generation` pipeline  
- Maintains conversation history with a sliding window buffer tracking the last 5 turns  
- Robust CLI supporting continuous user input  
- Clean and graceful exit by typing `/exit`  
- Modular Python codebase consisting of:  
  - `model_loader.py`: Responsible for loading the model pipeline  
  - `chat_memory.py`: Manages sliding window conversational memory  
  - `interface.py`: Integrates CLI with model and memory modules  

---

## 🛠️ Setup Instructions

1. **Clone the repository** or unzip the project folder.

2. **Create and activate a Python virtual environment** (recommended):

```
python -m venv .venv
```


3. **Install dependencies:**

```
pip install transformers torch
```


---

## ▶️ Running the Chatbot

Launch the chatbot CLI by executing:

```
python interface.py
```

You'll see a prompt like:

```
Starting Local CLI Chatbot. Type /exit to quit.
```

Simply type your message and press Enter. The bot will respond instantly, maintaining context from recent conversation turns.

---

## 📁 Project Structure

| File              | Description                                    |
|-------------------|------------------------------------------------|
| `model_loader.py` | Loads the Hugging Face model pipeline           |
| `chat_memory.py`  | Handles conversation memory with sliding window |
| `interface.py`    | CLI interface tying the model and memory together |
| `README.md`       | Project overview, setup guide, and usage instructions |

---

## 📝 Additional Notes

- The conversation history is intelligently truncated to fit within model input limits, preventing errors.  
- The model runs efficiently on CPU; GPU support is optional.  
- Designed for clarity, maintainability, and easy future enhancements.

---

## 🙋 Author

**Om Jaikumar**

---

Thank you for exploring this chatbot project! Feel free to contribute or customize it to your needs. 🚀


