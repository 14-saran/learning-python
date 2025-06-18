#json
import json

employee = {
    "name" : "vodka",
    "age" : 30,
    "job" : "cook"
}

file_path = "C:/Users/saran/OneDrive/Desktop/output.json"

#with open(file=file_path,mode= "w") as file:

with open(file_path, "w") as file:
    json.dump(employee, file, indent=4)
    print(f"json file '{file_path}' was created")