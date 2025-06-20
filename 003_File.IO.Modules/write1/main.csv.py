#.csv
import csv

employee = [["name", "age", "job"],
            ["A", "24", "cook"],
            ["B", "26", "unemployed"],
            ["C", "28", "docter"]]


file_path = "C:/Users/saran/OneDrive/Desktop/output.csv"

#with open(file=file_path,mode= "w") as file:
with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)
    for row in employee:
        writer.writerow(row)
    print(f"csv file '{file_path}' was created")