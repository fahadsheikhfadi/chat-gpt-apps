import openai
import tkinter as tk
from tkinter import scrolledtext

# Replace YOUR_API_KEY with your actual API key
openai.api_key = "API_KEY_HERE"

def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,  # Increase the max_tokens value
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = response.choices[0].text.strip()
    return message

def format_conversation_history(history):
    formatted_history = ""
    for idx, message in enumerate(history):
        sender = "You" if idx % 2 == 0 else "AI"
        formatted_history += f"{sender}: {message}\n"
    return formatted_history

def send_message(event=None):
    user_input = user_input_box.get()
    user_input_box.delete(0, tk.END)

    if user_input.lower() == "exit":
        root.quit()

    conversation_history.append(user_input)
    chat_history.config(state="normal")
    chat_history.insert(tk.END, f"You: {user_input}\n")

    prompt = format_conversation_history(conversation_history)
    prompt += "AI:"
    generated_text = generate_text(prompt)
    conversation_history.append(generated_text)
    chat_history.insert(tk.END, f"AI: {generated_text}\n")
    chat_history.see(tk.END)
    chat_history.config(state="disabled")

# Create the main window
root = tk.Tk()
root.title("GPT-4 Chat App")

# Create the chat history widget
chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, state="disabled")
chat_history.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Create the user input widget
user_input_box = tk.Entry(root, width=50)
user_input_box.grid(row=1, column=0, padx=10, pady=10)
user_input_box.bind("<Return>", send_message)

# Create the send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Initialize the conversation history
conversation_history = []

# Start the GUI event loop
root.mainloop()
