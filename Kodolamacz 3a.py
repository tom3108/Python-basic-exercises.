# x podaj jako string
def czyPalindrom(x):
    a = x
    b = x [::-1]
    if a == b:
        print (True)
    else:
        print (False)

czyPalindrom("kajak")
czyPalindrom("malar")
czyPalindrom("malam")


