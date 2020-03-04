def czyAnagram(napis1 , napis2):
    n = len(napis1)
    if n != len(napis2):
        return print(False)
    else:
        slownik1 = dict()
        slownik2 = dict()
        for x in range(n):
            if napis1[x] in slownik1:
                slownik1[napis1[x]] += 1
            else:
                slownik1[napis1[x]] = 1
            if napis2[x] in slownik2:
                slownik2[napis1[x]] += 1
            else:
                slownik2[napis2[x]] = 1
        return print(slownik1 == slownik2)

czyAnagram("kraby", "rybak")
czyAnagram("kqaby", "rybak")
czyAnagram("akqaby", "rybak")