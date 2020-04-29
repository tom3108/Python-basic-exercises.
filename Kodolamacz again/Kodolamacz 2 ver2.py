parametr= True

while parametr:
    print("Podaj w oddzielnych wierszach liczbę, operację matematyczną: +,-,*,/,%, a następnie kolejną liczbę:")
    liczba1 = float(input("Wprowadź pierwszą liczbę:"))
    operacja = input("Wprowadź operację:")
    liczba2 = float(input("Wprowadź drugą liczbę:"))

    if operacja == "+":
        wynik = liczba1 + liczba2
        print("Twój wynik to:", wynik)
    elif operacja == "-":
        wynik = liczba1 - liczba2
        print("Twój wynik to:", wynik)
    elif operacja == "*":
        wynik = liczba1 * liczba2
        print("Twój wynik to:", wynik)
    elif operacja == "/":
        wynik = liczba1 / liczba2
        print("Twój wynik to:", wynik)
    elif operacja == "%":
        wynik = liczba1 % liczba2
        print("Twój wynik to:", wynik)
    else:
        print("Wprowadź poprawną operację")
        continue

    print("Chcesz wykonać operację ponowanie? Wpisz t/n")
    again = input("Wykonać obliczenia ponownie?")

    if again == "t":
        parametr = True
    elif again == "n":
        parametr = False
