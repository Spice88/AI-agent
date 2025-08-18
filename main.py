import os
from dotenv import load_dotenv
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai

client = genai.Client(api_key=api_key)

def main():
    print("Hello from ai-agent!")


if __name__ == "__main__":
    main()

if len(sys.argv) > 1:
    prompt = sys.argv[1]
else:
    print("No prompt provided.")
    sys.exit(1)
ai_response = client.models.generate_content(model="gemini-2.0-flash-001", contents=prompt)

print(ai_response.text)
print(f"Prompt tokens: {ai_response.usage_metadata.prompt_token_count}")
print(f"Response tokens: {ai_response.usage_metadata.candidates_token_count}")