""""
Easier and more readable loop
"""

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# my_list = list(map(lambda n: n, nums))

my_list = [n for n in nums if n%2 == 0]

print(my_list)