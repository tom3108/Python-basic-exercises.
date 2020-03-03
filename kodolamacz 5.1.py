from abc import ABC, abstractmethod
import math

class Figura (ABC):
    @abstractmethod
    def nazwa(self):
        pass
    @abstractmethod
    def obwod(self):
        pass
    @abstractmethod
    def pole(self):
        pass

    def wypisz(self):
        print(f"Jestem {self.nazwa()}. Moj obwod: {self.obwod()}, a pole: {self.pole()}.")

class Trojkat(Figura):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def nazwa(self):
        return "trojkat"
    def obwod(self):
        return self.a + self.b + self.c
    def pole(self):
        p = self.obwod() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

class Kolo(Figura):
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
    def nazwa(self):
        return "kolo"
    def obwod(self):
        return 2 * math.pi * self.r
    def pole(self):
        return math.pi * self.r ** 2

def main():
    t = Trojkat(3.0, 4.0, 5.0)
    t.wypisz()
    k = Kolo(4, 5, 1)
    k.wypisz()

    lista_figur = [t, k]
    suma_pol = 0
    suma_obwodow = 0
    for f in lista_figur:
        suma_pol += f.pole()
        suma_obwodow += f.obwod()

    print(suma_pol)
    print(suma_obwodow)

if __name__ == "__main__":
    main()