def moda(list):
    #parametrem tej funkcji jest lista liczb
    slownik = dict()
    for i in list:
        if i in slownik:
            slownik[i] += 1
        else:
            slownik[i] = 1
    print(slownik.items())

    maks = -1
    liczba_maks = -1

    for (co, ile) in slownik.items():
        if ile > maks:
            liczba_maks = co
            maks = ile
    return print("Najcześciej występująca liczba w podanej liście to", liczba_maks)



#moda([3,5,1,3,5,4,3,2,5,6,3,4,5,6,1,2,3,1])
moda([1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2])