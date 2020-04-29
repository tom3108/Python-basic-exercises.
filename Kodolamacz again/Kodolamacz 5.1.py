from abc import ABC, abstractmethod
import math

class Figura (ABC):
    @abstractmethod
    def nazwa (self):
        pass
    @abstractmethod
    def obwod (self):
        pass
    @abstractmethod
    def pole (self):
        pass
    def wypisz(self):
        print(f"Jestem {self.nazwa()}. Moj obwod: {self.obwod()}, a pole:{self.pole()}")

class Trojkat (Figura):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def nazwa(self):
        return "trójkąt"
    def obwod(self):
        return  self.a + self.b + self.c
    def pole(self):
        p = self.obwod() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

trojkat1 = Trojkat(4,5,6)
print(trojkat1.nazwa())
print(trojkat1.obwod())
print(trojkat1.pole())
trojkat1.wypisz()