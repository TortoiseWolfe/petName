import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def refactor_code(code):
    prompt = f"Refactor the following Python code to make it more efficient and readable, and provide a summary of the changes made:\n\n{code}\n\nRefactored code:\n\nSummary of changes:"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=3500,
        n=1,
        stop=None,
        temperature=0.2,
    )

    response_text = response.choices[0].text.strip()
    
    # Find the position of the double newline in the response_text
    double_newline_pos = response_text.find("\n\n")

    # If the double newline is found, separate the summary and refactored code
    if double_newline_pos != -1:
        summary = response_text[:double_newline_pos].strip()
        refactored_code = response_text[double_newline_pos:].strip()
    else:
        refactored_code = response_text
        summary = "Summary not available."

    return refactored_code, summary

def process_files(folder_path, output_folder="./refactored"):
    for file_name in os.listdir(folder_path):
        print(f"Found file: {file_name}")
        if file_name.endswith(".py"):
            with open(os.path.join(folder_path, file_name), "r") as file:
                code = file.read()
                refactored_code, summary = refactor_code(code)
                print(f"Refactored code for {file_name}:\n{refactored_code}\n")
                print(f"Summary of changes for {file_name}:\n{summary}\n")

            # Save the refactored code to a new file or overwrite the original file
            os.makedirs(output_folder, exist_ok=True)
            with open(os.path.join(output_folder, file_name), "w") as file:
                file.write("# Summary of changes:\n")
                file.write("\n".join([f"# {line}" for line in summary.split("\n")]))
                file.write("\n\n")
                file.write(refactored_code)

if __name__ == "__main__":
    process_files("./repofolder")
