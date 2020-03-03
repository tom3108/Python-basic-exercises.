import  math

class FunkcjaKwadratowa ():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def wypisz(self):
        print(f"{self.a}*x^2 + {self.b}*x + {self.c}")
        #print(self.a,"x^2 +",self.b,"x", self.c )

    def oblicz_wartosc(self, x):
        return self.a * x * x + self.b * x + self.c

    def rozwiaz(self):
        if self.a == 0:
            return print("To nie jest funkcja kwadratowa")
        else:
            delta = self.b**2 - 4*self.a*self.c
            if delta > 0 :
                r1 = (-self.b - pow(delta, 0.5))/2*self.a
                r2 = (-self.b + pow(delta, 0.5)) / 2 * self.a
                return r1, r2
            elif delta == 0:
                r0 = -self.b/2*self.a
                return r0
            else:
                return print("Brak rozwiązań")
def main ():
    f1 = FunkcjaKwadratowa(1, 4, -3)
    f1.wypisz()
    print(f1.oblicz_wartosc(1))
    print(f1.oblicz_wartosc(2))

    print(FunkcjaKwadratowa(1,4,-3).rozwiaz())
    print(FunkcjaKwadratowa(1, 4, 3).rozwiaz())
    print(FunkcjaKwadratowa(0, 4, -3).rozwiaz())
    print(FunkcjaKwadratowa(1, 4, 4).rozwiaz())
    print(FunkcjaKwadratowa(7, 25, 4).rozwiaz())
    #print(FunkcjaKwadratowa(1, 5, 25).rozwiaz())


if __name__ == "__main__":
    main()

