from abc import ABC, abstractmethod

import math

class Wezel (ABC):
    @abstractmethod
    def nazwa(self):
        pass
    def wypisz (self):
        print(f"Wykonuję {self.nazwa()}.", end=" ")
    @abstractmethod
    def wartosc(self):
        pass

class Liczba(Wezel):
    def __init__(self, liczba):
        self.liczba = liczba

    def nazwa(self):
        return "liczba"

    def wypisz(self):
        print(f"Jestem liczbą")