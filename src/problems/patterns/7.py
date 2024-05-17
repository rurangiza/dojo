"""
size = 5

    #      1
   ###     3
  #####    5
 #######   7
#########  9
"""

size = int(input("Size: "))
# for i in range(size):
#     if i % 2 == 0:
#         continue
#     mid = (size - i) // 2
#     print(f'{" " * mid}{"#" * i}{" " * mid}')
    

for i in range(size):
    if i % 2 == 0:
        continue
    for j in range(size):
        start = (size - j) // 2
        end = start + i
        if end > j >= start:
            print("#", end="")
        else:
            print(" ", end="")

