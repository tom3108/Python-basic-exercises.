
def czyAnagram(napis1, napis2):
    #Jako argumenty funkcji podaj string
    list1 = []
    list2 = []
    for a in napis1:
        list1.append(a)

    for b in napis2:
        list2.append(b)

    list1.sort()
    list2.sort()
    if list1 == list2:
        print("Podane napisy to anagramy")
    else:
        print("Podane napisy to nie anagramy")

czyAnagram("optyczny","poczytny")
czyAnagram("tomek","kemot")
czyAnagram("anonim","anonimus")

