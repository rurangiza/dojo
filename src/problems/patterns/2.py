"""
size = 5

#
##
###
####
#####
"""

size = int(input("Size: "))
for i in range(1, size+1):
    print("#" * i)

# or
# for i in range(size+1):
#     for j in range(i+1):
#         print("#", end="")
#     print()