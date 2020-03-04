class Ulamek():
    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik
    def wypisz(self):
        print(f" {self.licznik}/{self.mianownik}")
    @staticmethod
    def dodaj (u1 , u2):
        lewy_licznik = u1.licznik * u2.mianownik
        prawy_licznik = u2.licznik * u1.mianownik
        wynik = Ulamek(lewy_licznik + prawy_licznik, u1.mianownik * u2.mianownik)
        return wynik

def main():
    u1 = Ulamek(7, 4)
    u2 = Ulamek(11, 6) # nieskrocony
    u1.wypisz()
    u2.wypisz()

    print("Dodawanie")
    Ulamek.dodaj(u1, u2).wypisz()



if __name__ == "__main__":
   main()
