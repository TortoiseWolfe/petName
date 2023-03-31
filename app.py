import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_pet_name():
    prompt = "Generate a creative and unique pet name:"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=10,
        n=1,
        stop=None,
        temperature=0.7,
    )

    pet_name = response.choices[0].text.strip()
    return pet_name

if __name__ == "__main__":
    print(generate_pet_name())
