class Ulamek():
    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik
    def wypisz (self):
        return f"{self.licznik}/{self.mianownik}"
    @staticmethod
    def dodaj (u1, u2):
        wsp_mian = u1.mianownik * u2.mianownik
        licznik_og = u2.mianownik * u1.licznik + u1.mianownik * u2.licznik
        return print(f"{licznik_og}/{wsp_mian}")


u1 = Ulamek(7, 4)
u2 = Ulamek(11, 6)
print(u1.wypisz())
print(u2.wypisz())
print("Dodawanie")
Ulamek.dodaj(u1,u2)

