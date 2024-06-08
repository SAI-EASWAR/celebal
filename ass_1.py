
for i in range(5):
    for j in range(i):
        print("*",end=" ")
    print()

for i in range(5, 0, -1):  # Corrected range to count downwards from 5 to 1
    for j in range(5-i):
        print(" ",end="")
    for j in range(i):
        print("*", end="")
    print()



for i in range(5):
    for j in range(5 - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()