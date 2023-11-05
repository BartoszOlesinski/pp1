x = int(input('Podaj numer: '))
y = int(input('Podaj numer: '))

if x >= 0 or y >= 0:
    print(f'At least one of entered numbers {x} and {y} nie jest negatywny')
else:
    print(f'Both number are negative')