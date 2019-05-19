height = int(input("number of steps"))
for i in range(height):
    spaces = height - i
    hashes = i + 1
    for k in range((spaces - 1)):
        print(" ", end ='')
    for j in range((hashes + 1)):
        print("#", end ='')
    print("\n")