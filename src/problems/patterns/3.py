"""
size = 5

1
12
123
1234
12345
"""
size = int(input("Size: "))
for i in range(1, size+1):
    for j in range(1, i+1):
        print(j, end="")
    print()