waga = int(input("Podaj swoja wagę: "))
wzrost = int(input("Podaj swój wzrost: "))

bmi = waga/(wzrost*0.01)**2

print(f"Twoje BMI wynosi: {bmi}\nJest prawidłowe {18.5<bmi<24.99}")