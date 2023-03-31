import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def refactor_code(code):
    prompt = f"Refactor the following Python code to make it more efficient and readable:\n\n{code}\n\nRefactored code:"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=3500,
        n=1,
        stop=None,
        temperature=0.2,
    )

    refactored_code = response.choices[0].text.strip()
    return refactored_code


def extract_summary(code, refactored_code):
    prompt = f"Given the following original code:\n\n{code}\n\nAnd the refactored code:\n\n{refactored_code}\n\nProvide a summary of the changes made:"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.2,
    )

    summary = response.choices[0].text.strip()
    return summary


folder_path = "./repofolder"
refactored_folder = "./refactored"

# Create the refactored folder if it doesn't exist
if not os.path.exists(refactored_folder):
    os.makedirs(refactored_folder)

for file_name in os.listdir(folder_path):
    print(f"Found file: {file_name}")
    if file_name.endswith(".py"):
        with open(os.path.join(folder_path, file_name), "r") as file:
            code = file.read()
            refactored_code = refactor_code(code)
            summary = extract_summary(code, refactored_code)
            print(f"Refactored code for {file_name}:\n{refactored_code}\n")
            print(f"Summary of changes for {file_name}:\n{summary}\n")

        # Save the refactored code to a new file in the refactored folder
        with open(os.path.join(refactored_folder, file_name), "w") as file:
            file.write(refactored_code)
