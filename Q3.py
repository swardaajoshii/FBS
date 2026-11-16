
for i in range(12):
    for j in range(23):
        if (i == 0 or i == 11) and j < 22:
            print("*", end=" ")
        elif j == 23 - i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
