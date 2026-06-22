# 🔍 AI Code Reviewer

### AI-powered code review using Groq LLaMA 3.3

Analyze code for **bugs**, **security vulnerabilities**, **performance issues**, and **style improvements** in seconds.

## 🌐 Live Demo

👉 https://ai-code-reviewer-1306.streamlit.app/

## 📸 Preview


![AI Code Reviewer](screenshot.png)

---

## ✨ Key Features

### ✅ Syntax-highlighted code editor

### ✅ Multi-language support

* Python
* JavaScript
* Java
* C++
* C#
* Go
* Ruby
* Other Languages

### ✅ AI-powered review using Groq LLaMA 3.3

### ✅ Detects

* Bugs & logical errors
* Security vulnerabilities
* Performance bottlenecks
* Code style issues

### ✅ Beginner-friendly explanations

### ✅ Download review reports

### ✅ Docker support

---

## 🏗️ How It Works

```text
Paste Code
    ↓
Select Language
    ↓
Groq LLaMA 3.3
    ↓
AI Analysis
    ↓
Review Report
```

---

## 🛠️ Tech Stack

| Category         | Technology                |
| ---------------- | ------------------------- |
| Language         | Python                    |
| Frontend         | Streamlit                 |
| AI Model         | Groq LLaMA 3.3            |
| Editor           | streamlit-ace             |
| Deployment       | Streamlit Community Cloud |
| Containerization | Docker                    |
| Version Control  | Git & GitHub              |

---

## ⚡ Quick Start

### Clone Repository

```bash
git clone https://github.com/medhaveeraiyan-rgb/ai-code-reviewer.git
cd ai-code-reviewer
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure API Key

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

### Run Application

```bash
streamlit run app.py
```

---

## 🐳 Docker

### Build Image

```bash
docker build -t ai-code-reviewer .
```

### Run Container

```bash
docker run -p 8501:8501 --env-file .env ai-code-reviewer
```

---

## 🚀 Roadmap

*  Review History
*  Code Quality Score
*  PDF Export
*  GitHub Integration
*  Multiple LLM Providers
*  Analytics Dashboard

---

## 👥 Contributors

* **Medha V** (@medhaveeraiyan-rgb)
* **Harini** (@Harini696)

---

## 📄 License

MIT License

---

⭐ If you found this project useful, consider giving it a star.
