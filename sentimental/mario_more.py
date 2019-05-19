height = int(input("number of steps"))
for i in range(height):
    spaces = height - i
    hashes = i + 1
    for k in range((spaces - 1)):
        print(" ", end ='')
    for j in range((hashes)):
        print("#", end ='')
    print("  ", end ='')
    for l in range((hashes)):
        print("#", end ='')
    print("\n")