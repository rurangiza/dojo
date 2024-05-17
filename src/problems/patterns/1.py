"""
size = 5

#####
#####
#####
#####
#####
"""

size = int(input("Size: "))
for i in range(size):
    print("#" * size)

"""
or nested loop
"""
# for i in range(size):
#     for j in range(size):
#         print("#", end="")
#     print("")