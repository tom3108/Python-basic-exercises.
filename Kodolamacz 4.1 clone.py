import math

class FunkcjaKwadratowa():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def wypisz_funk(self):
        print(f"Badana funkcja kwadratowa: {self.a}x^2 + {self.b}x + {self.c}")
    def oblicz_funk(self, x):
        return print(self.a * x * x + self.b * x + self.c)
    def rozwiaz_funk(self):
        delta = pow(self.b, 2) - 4 * self.a * self.c

        if self.a == 0:
            print("To nie jest funkcja kwadratowa")
        else:
            if delta > 0:
                r1 = (-self.b - pow(delta, 0.5)) / 2 * self.a
                r2 = (-self.b + pow(delta, 0.5)) / 2 * self.a
                return print(r1, r2)
            elif delta == 0:
                r0 = -self.b / 2 * self.a
                return print(r0)
            else:
                return print("Brak rozwiązań")

def main ():
    f1 = FunkcjaKwadratowa(1, 2, 9)
    f1.wypisz_funk()
    f1.oblicz_funk(2)
    f1.rozwiaz_funk()

    print(FunkcjaKwadratowa(1, 3, -4).wypisz_funk())
    print(FunkcjaKwadratowa(1, 3, -4).oblicz_funk(1))
    print(FunkcjaKwadratowa(1,3,-4).rozwiaz_funk())




if __name__ == "__main__":
    main()








