import random
kostka = random.randint(1,6)
zgd = int(input("Zgadnij numer od 1 do 6: "))

print(f"Zgadłeś: {kostka == zgd}")