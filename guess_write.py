import csv

'''
with open("best_scores.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["100"])
'''

from random import randint

attempt = 0
max_attempt = 100
poruka1 = "Broj je veći od zamišljenog..."
poruka2 = "Broj je manji od zamišljenog..."
poruka3 = "Bravo, pogodili ste zamišljen broj!"
poruka4 = "Iskoristili ste max broj pokušaja"

print("Igra pogađanja zamišljenog broja u rasponu 1-100...")
secret = randint(1, 100)
best_score = 100

with open("best_scores.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        if best_score > int(row[0]):
            best_score = int(row[0])
    file.close()
print(f"Dosadašnji najbolji rezultat iznosi pogodak iz {best_score} pokušaja")

while attempt <= max_attempt:
    guess = int(input("Probajte pogoditi zamišljeni broj: "))
    attempt += 1
    if guess == secret:
        print(poruka3)
        print(f"Imali ste {attempt} pokušaja")
        with open("best_scores.csv", "r") as file:
            best_score_record = csv.reader(file)
            for row in best_score_record:
                if attempt < int(row[0]):
                    best_score = attempt
                    with open("best_scores.csv", "w", newline="") as scores:
                        write = csv.writer(scores)
                        write.writerow(str(attempt))
                        scores.close()
            file.close()
        if attempt == max_attempt:
            print(poruka4)
        break
    elif guess > secret:
        print(poruka2)
        print(f"Imali ste {attempt} pokušaja")
        print(f"Preostalo Vam je {max_attempt - attempt} pokušaja\n")
        if attempt == max_attempt:
            print(poruka4)
            break
    elif guess < secret:
        print(poruka1)
        print(f"Imali ste {attempt} pokušaja")
        print(f"Preostalo Vam je {max_attempt - attempt} pokušaja\n")
        if attempt == max_attempt:
            print(poruka4)
            break
