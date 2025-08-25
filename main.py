import os
from dotenv import load_dotenv
import sys
from google import genai
from google.genai import types

#Get API key from .env
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

#Original main.py function text
def main():
    print("Hello from ai-agent!")
    client = genai.Client(api_key=api_key)

    #Exit if prompt not provided
    if len(sys.argv) > 1:
        user_prompt = sys.argv[1]
    else:
        print("No prompt provided.")
        sys.exit(1)

    ai_response = client.models.generate_content(model="gemini-2.0-flash-001", contents=user_prompt)

#New list of types.Content - user's prompt is currently the only message
    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)]),]

#Update call to models.generate_content to use the messages list
    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages,)

    if "--verbose" in sys.argv:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {ai_response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {ai_response.usage_metadata.candidates_token_count}")
        print(ai_response.text)
    else:
        print(ai_response.text)

if __name__ == "__main__":
    main()
