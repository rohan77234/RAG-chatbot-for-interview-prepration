import os
import sys
import subprocess
import time
import gradio as gr
from ollama import generate


class InterviewBot:
    def __init__(self):
        self.model = "mistral"

        # Ensure Ollama is installed and running
        try:
            generate(model=self.model)
        except Exception as e:
            print("Installing Ollama Python package...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "ollama"])

            # Wait for Ollama server to start
            time.sleep(3)

        # Initialize KT and retrieve data
        try:
            kt_response = self.get_kt_data()
        except Exception as e:
            print(f"Error retrieving data via Knowledge Template: {str(e)}")

    def get_kt_data(self):
        import json
        with open('kt.json') as f:
            return json.load(f)

    def respond(self, message, history):
        # Retrieve data via KT and use indexing to feed it into Ollama
        kt_data = self.get_kt_data()

        try:
            # Generate response using Ollama
            response = generate(
                model=self.model,
                prompt=f"""
                    You are Rohan Sharma answering interview questions.
                    Respond to this professionally in 2-3 sentences:

                    Question: {message}

                    Answer:""",
                options={'temperature': 0.5, 'indexing': kt_data},
            )
            return response['response']
        except Exception as e:
            return f"Error generating response: {str(e)}\n\nTry running 'ollama serve' in another terminal."


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
    iface.launch(share=True)
