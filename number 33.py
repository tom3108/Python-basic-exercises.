def AB (x,y,z):
    if x == y or y == z or x == z:
        sum = 0
        return sum
    else:
        sum = x + y + z
        return sum

print(AB(5,10,15))

print(AB(15,10,15))

print(AB(5,5,15))

