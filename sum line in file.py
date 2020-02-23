
def sumLines():
    a = open("C:\\Users\\Tomek\\Desktop\\Python tasks\\tekst.txt").read().splitlines()
    sum = 0
    for b in a:
        sum += 1
    return sum

print(sumLines())
