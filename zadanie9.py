print("Witam w kalkulatorze, wybierz liczbę przypisaną do działania. \n"
      "1. Dodawanie \n"
      "2. Odejmowanie \n"
      "3. Mnożenie \n"
      "4. Dzielenie \n"
      "5. Potęgowanie \n")
typ_dzialania = input()

if typ_dzialania == "1":
    a = float(input("Podaj pierwszą liczbę: "))
    b = float(input("Podaj drugą liczbę: "))
    print(f"Wynik dodawania to: {a+b}")
elif typ_dzialania == "2":
    a = float(input("Podaj pierwszą liczbę: "))
    b = float(input("Podaj drugą liczbę: "))
    print(f"Wynik odejmowania to: {a - b}")
elif typ_dzialania == "3":
    a = float(input("Podaj pierwszą liczbę: "))
    b = float(input("Podaj drugą liczbę: "))
    print(f"Wynik mnożenia to: {a * b}")
elif typ_dzialania == "4":
    a = float(input("Podaj pierwszą liczbę: "))
    b = float(input("Podaj drugą liczbę: "))
    if b!=0:
        print(f"Wynik dzielenia to: {a / b}")
    else:
        print("Nie można dzielić przez zero, spróbuj ponownie.")
elif typ_dzialania == "5":
    a = float(input("Podaj liczbę: "))
    b = float(input("Podaj jej potęgę: "))
    print(f"Wynik potęgowania to: {a ** b}")
else:
    print("Podałeś niepoprawny numer działania, spróbuj ponownie.")
