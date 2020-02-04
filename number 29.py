color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

for a in color_list_1:
    if a not in color_list_2:
        print(a)