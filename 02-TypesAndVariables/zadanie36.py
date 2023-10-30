bankbuy = float(input("Podaj za ile bank kupuje euro: "))
banksell = float(input("Podaj za ile bank sprzedaje euro: "))
spread = banksell-bankbuy
print(f"Bank kupuje euro za: {bankbuy}\na sprzedaję za: {banksell}\nRóżnica pomiędzy kupna a sprzedażą wynosi: {round(spread, 4)}")