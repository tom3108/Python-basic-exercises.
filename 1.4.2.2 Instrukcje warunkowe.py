import math

op = "t"

while op == "t":

    a, b, c =  input("Podaj trzy boki trójkąta oddzielone /").split("/")
    a = int(a)
    b = int (b)
    c= int (c)
    if a + b > c and a + c > b and b + c > a:
        print("Z podanych boków można zbudować trójkąt")
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2:
            print("Obwód trójkąta =", a + b + c)
    else:
        print("Z podanych boków nie można zbudować trójkąt")
    op = input("Again? t/n")