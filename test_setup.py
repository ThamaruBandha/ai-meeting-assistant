import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

# Connect to Groq using your key
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Same request/response pattern as before, just pointed at Groq's servers
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    max_tokens=50,
    messages=[{"role": "user", "content": "Say 'connection successful' and nothing else."}]
)

print(response.choices[0].message.content)