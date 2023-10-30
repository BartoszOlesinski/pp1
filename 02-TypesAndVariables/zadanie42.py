#z funkcja 
#a = input("Podaj liczbę binarną: ")
#b = int(a[0:4], 2)
#print(f"Numer binarny {a[0:4]}\nLiczba w systemie dziesiętnym wynosi: {b}")

#bez funkcji 
liczba = input("Podaj liczbę: ")
liczba = liczba[0:4]
a = 4 - 1
sum = 0

for i in liczba:
    if i == "1":
        sum += 1 * 2 ** a
    a -= 1

print(f"Liczba binarną: {liczba}\nDziesiętny: {sum}")