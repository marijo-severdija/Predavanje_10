import csv

'''with open("person.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Tina", "23", "female"])
    writer.writerow(["Jakob", "35", "male"])
    writer.writerow(["Barbara", "44", "female"])
file.close()'''

with open("person.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"{row[0]} is {row[1]} years old and {row[2]}")
