"""
size = 5
######### 0
 #######  2
  #####
   ###
    #
"""
size = 10
for i in range(size):
    curr = size - i
    if curr % 2 == 0:
        continue
    for j in range(size):
        if j < curr:
            print("#")
    