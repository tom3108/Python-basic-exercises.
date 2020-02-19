def moda(lista):
    slownik = dict()
    n = len(lista)
    for a in range(n):
        if lista[a] in slownik:
            slownik[lista[a]] += 1
        else:
            slownik[lista[a]] = 1
    print(slownik)

moda([3,4,1,2,31,3,4,1,23,41,2,1])