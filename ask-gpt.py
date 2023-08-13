import os
import openai
import key

key.setenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def chatMsg(prompt):
    completion =openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return completion.choices[0].message["content"]

if __name__ == "__main__":
    prompt = "2023年4月現在の首相の名前は何でしょうか"
    result = chatMsg(prompt)
    print(result)