# Python reading files (.json)

import json
file_path = "C:/Users/saran/OneDrive/Desktop/output.json"

try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("you do not need have permission to read that file")