# AI-Powered Browser Agent

## 🚀 Overview
This project is an AI-powered browser automation agent that takes user input for tasks, processes them using OpenAI's GPT model, and executes them using `browser-use`. The agent is capable of navigating websites, extracting data, and automating tasks based on AI-generated commands.

## 🛠️ Tech Stack
- **Python**
- **LangChain**
- **OpenAI GPT-4o**
- **Browser-Use Agent**
- **Dotenv (for environment variables)**
- **Playwright (for browser automation)**

## 📂 Project Structure
```
📁 project-directory
│── agent.py            # Main script to run the AI agent
│── .env                # Environment variables (API keys)
│── README.md           # Project documentation
```

## 🔧 Setup Instructions
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/your-repository.git
cd your-repository
```

### 2️⃣ Install Dependencies
```sh
pip install langchain langchain_openai browser-use python-dotenv playwright gradio
```

### 3️⃣ Install Playwright
```sh
playwright install
```

### 4️⃣ Set Up Environment Variables
Create a `.env` file and add your OpenAI API key:
```
OPENAI_API_KEY=your-api-key
```

### 5️⃣ Run the AI Agent
```sh
python agent.py
```

## 🎯 Quick Start Example
```python
from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv

load_dotenv()

async def main():
    agent = Agent(
        task="Go to Reddit, search for 'browser-use', click on the first post and return the first comment.",
        llm=ChatOpenAI(model="gpt-4o"),
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
```

## 🎯 Test with UI
You can test `browser-use` with a UI repository.
Or simply run the Gradio example:
```sh
pip install gradio
python examples/ui/gradio_demo.py
```

## 🔍 Example Usage
```
Whatup man? Go to YouTube and find the first trending video.
```
*Output: The agent fetches the trending video and returns details.*

## 🛠️ Troubleshooting
- **Error: `ModuleNotFoundError`?**
  - Ensure all dependencies are installed: `pip install langchain langchain_openai browser-use python-dotenv playwright gradio`
- **Error: API key issue?**
  - Double-check `.env` file and API key validity.
- **Playwright not working?**
  - Run `playwright install` to install required browser dependencies.

## 📜 License
This project is licensed under the **Apache License**.

---

🔹 **Contributions & Issues:** Feel free to contribute or report issues on GitHub!

