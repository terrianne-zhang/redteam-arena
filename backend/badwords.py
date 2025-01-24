import gradio as gr
import random
import time
from openai import OpenAI, models
from dotenv import load_dotenv
import os
from typing import List, Dict, Iterable


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

# Function to handle the chatbot's response generation
def bot(chat_history: list):
    user_message = chat_history[-1][0]  # Get the last user message
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}],
        stream=True,
    )
    bot_message = ""

    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            bot_message += chunk.choices[0].delta.content
            print(chunk.choices[0].delta.content, end="")
        chat_history[-1] = (chat_history[-1][0], bot_message)
        yield chat_history  # Yield updated chat history
        time.sleep(0.05)  # Simulate typing delay

# Function to handle user input submission
def user(user_message, chat_history: list):
    chat_history.append((user_message, ""))  # Add the user's message to chat history
    return "", chat_history

# Define the Gradio Blocks interface
with gr.Blocks() as demo:
    chatbot = gr.Chatbot()  # Chatbot interface
    msg = gr.Textbox(placeholder="Enter your message here...", label="Your Message")  # User input
    clear = gr.Button("Clear")  # Button to clear messages
    
    # Connect the message input and chatbot
    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
        bot, chatbot, chatbot  # Connect the bot function with streaming enabled
    )
    
    # Clear the chatbot history
    clear.click(lambda: None, None, chatbot, queue=False)

# Launch the Gradio app
demo.launch(share=True)  # Enable sharing for public testing





