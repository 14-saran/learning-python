# Python reading files (.txt)

file_path = "C:/Users/saran/OneDrive/Desktop/output.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("you do not need have permission to read that file")