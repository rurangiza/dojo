


N = int(input())
nums = [int(num) for num in input().split()]

def f(x, y):
    return (x + y) % 10**8

total = 0
for i in range(0, len(nums)-1):
    for j in range(i+1, len(nums)):
        curr = f(nums[i], nums[j])
        total += curr

print(total)

    