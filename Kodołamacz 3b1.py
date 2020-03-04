def czyAnagram(napis1 , napis2):
    #podaj argumenty jako napisy malymi literami
    list1 = []
    list2 = []
    for a in napis1:
        list1.append(a)
    for b in napis2:
        list2.append(b)
    list1.sort()
    list2.sort()


    if list1 == list2:
        print(True)
    else:
        print(False)


czyAnagram("kraby", "rybak")
czyAnagram("katar", "krata")
czyAnagram("kobra", "robak")
czyAnagram("lampa", "plama")
czyAnagram("lampa", "flama")


