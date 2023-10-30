nrrej = input("Podaj numer rejestracji auta: ")

x = nrrej[0:2]

print(f"Podana rejestracja {nrrej}")
print(f"Auto jest z krakowa: {x == 'KK' or x == 'KR'}")