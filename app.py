import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def refactor_code(code):
    prompt = f"Refactor the following Python code to make it more efficient and readable:\n\n{code}\n\nRefactored code:"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    refactored_code = response.choices[0].text.strip()
    return refactored_code

folder_path = "./repofolder"

for file_name in os.listdir(folder_path):
    print(f"Found file: {file_name}")  # Add this line to display the file names
    if file_name.endswith(".py"):
        with open(os.path.join(folder_path, file_name), "r") as file:
            code = file.read()
            refactored_code = refactor_code(code)
            print(f"Refactored code for {file_name}:\n{refactored_code}\n")

        # Save the refactored code to a new file or overwrite the original file
        with open(os.path.join("/refactored", file_name), "w") as file:
            file.write(refactored_code)
