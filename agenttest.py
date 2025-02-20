from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
import tkinter as tk
from tkinter import scrolledtext
from dotenv import load_dotenv

load_dotenv()

def run_agent():
    task = entry.get()
    output_text.delete(1.0, tk.END)  # Clear previous output
    
    async def main():
        agent = Agent(task=task, llm=ChatOpenAI(model="gpt-4o"))
        result = await agent.run()
        output_text.insert(tk.END, result)
    
    asyncio.run(main())

# Creating UI
root = tk.Tk()
root.title("LangChain Agent UI")
root.geometry("500x400")

tk.Label(root, text="Enter your task:").pack(pady=5)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

tk.Button(root, text="Run Agent", command=run_agent).pack(pady=10)

output_text = scrolledtext.ScrolledText(root, width=60, height=15)
output_text.pack(pady=5)

root.mainloop()
