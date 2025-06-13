import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    load_dotenv()

    print("AI Code Assistant")
    print("=================")
    print("Enter your prompt [--verbose]\n")
    
    try:
        verbose = "--verbose" in sys.argv
        args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
    except Exception as error:
        print("\nAn error occured:", error)
        print("Closing program...")
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY") # load the environment variables from .env file
    client = genai.Client(api_key=api_key) # new instance of a Gemini client

    user_prompt = " ".join(args)

    if verbose:
        print("User prompt: ", user_prompt)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    generate_content(client, messages, verbose)


def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages
    )
    print("Response:", response.text, end="")
    if verbose:
       print("Prompt tokens:", response.usage_metadata.prompt_token_count)
       print("Response tokens:", response.usage_metadata.candidates_token_count)
    

if __name__ == "__main__":
    main()
