def czyAnagram(napis1, napis2):
    n = len(napis1)
    if n != len(napis2):
        return False


    slownik1 =  dict()
    slownik2 = dict()
    
    for i in range(n):
        if napis1[i] in slownik1:
            slownik1[napis1[i]] += 1
        else:
            slownik1[napis1[i]] = 1

        if napis2[i] in slownik2:
            slownik2[napis2[i]] += 1
        else:
            slownik2[napis2[i]] = 1
    print(slownik1, slownik2)


    return print(slownik1 == slownik2, "%s oraz %s to anagramy" %(napis1,napis2))


czyAnagram("dsadas", "das")
czyAnagram("optyczny","poczytny")
czyAnagram("tomek","kemot")
czyAnagram("anonim","anonimus")
czyAnagram("yyyyzzzqq","qqzzzyyyy")