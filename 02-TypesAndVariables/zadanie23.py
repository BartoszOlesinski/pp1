a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))
obwt = a+b+c
polobwt = obwt/2
polewzorherona = (polobwt * (polobwt - a) * (polobwt - b) * (polobwt - c))** 0.5

print(f"Obwód trjkąta: {obwt}\npole trójkąta: {polewzorherona}")