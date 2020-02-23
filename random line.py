import random

def readRandom():
    a = open("C:\\Users\\Tomek\\Desktop\\Python tasks\\tekst.txt").read().splitlines()
    return random.choice(a)
print(readRandom())
