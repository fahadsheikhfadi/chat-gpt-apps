import openai
import sys

# Replace YOUR_API_KEY with your actual API key
openai.api_key = "API_KEY_HERE"

def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
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

def chat():
    print("Welcome to the GPT-4 Chat App! Type 'exit' to quit the app.")
    conversation_history = []

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        conversation_history.append(user_input)

        prompt = format_conversation_history(conversation_history)
        prompt += "AI:"
        generated_text = generate_text(prompt)

        conversation_history.append(generated_text)
        print(f"AI: {generated_text}")

if __name__ == "__main__":
    chat()
