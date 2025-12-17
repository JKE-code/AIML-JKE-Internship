# Jayanth

import requests

def call_ai_api(prompt):
    API_URL = "https://api.groq.com/openai/v1/chat/completions"
    API_KEY = "gsk_API_Key"  # replace with your Groq API key

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    print("STATUS CODE:", response.status_code)

    response.raise_for_status()

    data = response.json()
    return data["choices"][0]["message"]["content"]

prompt = "Explain the importance of Artificial Intelligence in one sentence."
reply = call_ai_api(prompt)

with open("ai_output.txt", "w", encoding="utf-8") as file:
    file.write("Prompt:\n")
    file.write(prompt + "\n\n")
    file.write("AI Response:\n")
    file.write(reply)

print("AI response saved successfully to ai_output.txt")

