"""
size = 5

1
22
333
4444
55555
"""

size =int(input("Size: "))
for i in range(1, size+1):
    print(str(i) * i)
