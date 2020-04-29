
def czyPalindrom(napis):
    list = []
    for litera in napis:
        list.append(litera)
    list2 = list.copy()
    list2.reverse()
    if list == list2:
        print("Wprowadzony napis to palindrom")
    else:
        print("Wprowadzony napis to nie palindrom")

czyPalindrom("kajak")
czyPalindrom("zakaz")
czyPalindrom("tomek")
czyPalindrom("radar")

