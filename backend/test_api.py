import os
from dotenv import load_dotenv
import groq

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
print(f"API Key: {api_key}")

try:
    client = groq.Client(api_key=api_key)
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": "Hello"}],
        max_tokens=10
    )
    print("Success!")
    print(response.choices[0].message.content)
except Exception as e:
    print(f"Error: {e}")