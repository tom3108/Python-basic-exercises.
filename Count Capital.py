with open("C:\\Users\\Tomek\\Desktop\\Python tasks\\tekst.txt", "r") as file:
    tekst = file.read()
    sum = 0
    for lett in tekst:
        if lett.isupper():
            sum += 1
    print("Plik tekst.txt zawiera " + str(sum) + " wielkich liter")

