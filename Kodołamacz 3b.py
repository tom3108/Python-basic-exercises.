
def czyAnagram(napis1 , napis2):
    suma = 0
    #podaj argumenty jako napisy malymi literami
    for a in napis2:
        if a in napis1:
            suma += 1

    if suma == len(napis2):
        print(True)
    else:
        print(False)

czyAnagram("kraby", "rybak")
czyAnagram("katar", "krata")
czyAnagram("kobra", "robak")
czyAnagram("lampa", "plama")
czyAnagram("laampa", "plama")
czyAnagram("ampa", "plama")
