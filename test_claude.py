import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

key = os.getenv("ANTHROPIC_API_KEY")
if not key:
    raise RuntimeError("Missing ANTHROPIC_API_KEY in .env")

client = Anthropic(api_key = key)

response = client.messages.create(
    model = "claude-haiku-5-5", max_tokens = 100, output_config = {"effort" : "low"},
    messages = [
        {
            "role": "user",
            "content" : "Say hello to my capstone team!"
        }
    ]
)

for block in response.content:
    if block.type == 'text':
        print(block.text)