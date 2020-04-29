import math

class FunkcjaKwadratowa():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def wypisz (self):
        return f"{self.a}*x^2 + {self.b}*x + {self.c}"

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




funk1 = FunkcjaKwadratowa(1, 2, -3)
print(funk1.wypisz())
print(funk1.oblicz_wartosc(5))
print(funk1.rozwiaz())

funk2 = FunkcjaKwadratowa(1, -3, -4)
print(funk2.wypisz())
print(funk2.oblicz_wartosc(10))
print(funk2.rozwiaz())