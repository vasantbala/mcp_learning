from dotenv import load_dotenv
import os
import openai

load_dotenv()

def main():
    client = openai.OpenAI(
        base_url="https://api.groq.com/openai/v1",
        api_key=os.environ.get("GROQ_API_KEY")
    )
    chat_completion = client.chat.completions.create(
    messages=[
            {
                "role": "user",
                "content": "Explain the importance of fast language models",
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    print(chat_completion.choices[0].message.content)

if __name__ == "__main__":
    main()
