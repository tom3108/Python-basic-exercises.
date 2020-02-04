def histogram (tup):
    empt = ""
    for t in tup:
        empt += (t * "@") + "\n"
    return empt

print(histogram((2,1,5)))
print("------------------")

print(histogram((4,1,5)))