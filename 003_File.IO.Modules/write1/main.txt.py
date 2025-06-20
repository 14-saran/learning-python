# Python writing files (.txt, json, .csv)

employees = ["Eguanu", "swana", "gogky" , "jemie"]
txt_data = "I like flowers."

file_path = "C:/Users/saran/OneDrive/Desktop/output.txt"

#with open(file=file_path,mode= "w") as file:
with open(file_path, "a") as file:
    for employee in employees:
        file.write(employee + " ")
    print(f"txt file '{file_path}' was created")

