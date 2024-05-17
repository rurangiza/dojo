"""
size = 5

#####
####
###
##
#
"""

size = int(input("Size: "))
for i in range(size):
    for j in range(1):
        print("#" * (size-i))