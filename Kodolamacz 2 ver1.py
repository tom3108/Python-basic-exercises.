#Prosty kalkulator

def main():

    again = "t"

    while "t" in again:
        liczba1 = float(input("Podaj pierwszą liczę:"))
        operacja = input("Wprowadź operację:")
        liczba2 = float(input("Podaj drugą liczę:"))

        if operacja == "+":
            wynik =  liczba1 + liczba2
        elif operacja == "-":
            wynik = liczba1 - liczba2
        elif operacja == "*":
            wynik = liczba1 * liczba2
        elif operacja == "/":
            wynik = liczba1 / liczba2
        elif operacja == "%":
            wynik = liczba1 % liczba2
        else:
            print("Błędna operacja")
            break
        print("Twój wynik to:" + str(wynik))
        print("Jezeli chcesz obliczyc ponowanie wpisz t, jezeli nie wpisz n")
        again = input("Chcesz obliczyc ponownie?")

main()
