imie = input("Imię pierwszej osoby: ")
lat = int(input('Podaj wiek pierwszej osoby: '))
imiex = input("Imię drugiej osoby: ")
latx = int(input('Podaj wiek drugiej osoby: '))

if lat >= 18 and latx >= 18:
    print(f'Oboje {imie} i {imiex} są dorośli')
else:
    print(f'Jedna osoba nie jest dorosły')