a = float(input("Podaj cenę produktu: "))
b = int(input("Podaj wielkość rabatu: "))

sum = a * (b*0.01)
sumpoobnizce = a-sum

print(f"Cena produktu: {a}\nWielkość rabatu %: {b}\nCena po obniżce: {round(sumpoobnizce, 2)}\nWielkość obniżki: {round(sum, 2)}")