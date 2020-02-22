#Pobierz od użytkownika trzy liczby, sprawdź, która jest najmniejsza i wydrukuj ją na ekranie.

op = "t"

while op == "t":

    a, b, c = input("Podaj trzy liczby oddzielone spacją:").split(" ")

    if int(a) < int(b) and int(a) < int(c):
        print("najmniejsza z podanych liczb to:", a)
    elif int(b) < int(a) and int(b) < int(c):
        print("najmniejsza z podanych liczb to:", b)
    else:
        print("najmniejsza z podanych liczb to:", c)

    op = input("Jeszcze raz? t/n")

print("The end")