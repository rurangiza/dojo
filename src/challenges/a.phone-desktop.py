"""
A. Phone Desktop
"""

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())

    remain = x + (4 * y)
    count = 0
    while remain > 0:
        desktop = 5 * 3
        while y > 0 and desktop >= 11:
            y -= 1
            remain -= 4
            desktop -= 4
        while desktop > 0 and x > 0:
            x -= 1
            remain -= 1
            desktop -= 1
        count += 1
    print(count)