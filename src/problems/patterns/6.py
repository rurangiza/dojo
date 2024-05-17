"""
size = 5

12345
1234
123
12
1
"""

size = int(input("Size: "))
for i in range(0, size):
    for j in range(1, size+1-i):
        print(j, end="")
    print()
