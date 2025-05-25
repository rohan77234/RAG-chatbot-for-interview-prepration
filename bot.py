# interview_bot.py
import os
import sys
import subprocess
import time
import gradio as gr


def ensure_ollama():
    try:
        import ollama
        return ollama
    except ImportError:
        print("Installing Ollama Python package...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "ollama"])
        import ollama
        return ollama


class InterviewBot:
    def __init__(self):
        self.ollama = ensure_ollama()
        self._start_ollama()
        self.model = "mistral"

    def _start_ollama(self):
        try:
            self.ollama.list()
        except:
            print("Starting Ollama server...")
            subprocess.Popen(["ollama", "serve"])
            time.sleep(3)  # Wait for server to start

    def respond(self, message, history):
        try:
            response = self.ollama.generate(
                model=self.model,
                prompt=f"""
                You are Rohan Sharma answering interview questions.
                Respond to this professionally in 2-3 sentences:

                Question: {message}

                Answer:""",
                options={'temperature': 0.5}
            )
            return response['response']
        except Exception as e:
            return f"Error: {str(e)}\n\nTry running 'ollama serve' in another terminal."


if __name__ == "__main__":
    iface = gr.ChatInterface(
        fn=InterviewBot().respond,
        title="Rohan's AI Interview Assistant",
        description="Ask about my skills, experience or projects",
        examples=[
            "What machine learning frameworks do you know?",
            "Tell me about your work at Fox Trading",
            "Describe your change detection project"
        ],
        theme=gr.themes.Soft()
    )
    iface.launch()