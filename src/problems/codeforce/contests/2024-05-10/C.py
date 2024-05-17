

t = int(input())
gi = lambda: list(map(int, input().strip().split()))

res = []

for i in range(t):
    a1, a2, b1, b2 = gi()

    tmp = a1
    a1 = max(a1, a2)
    a2 = min(tmp, a2)

    tmp2 = b1
    b1 = max(b1, b2)
    b2 = min(tmp2, b2)

    a1, a2, b1, b2 = [num if num > 6 else num+12 for num in [a1, a2, b1, b2]]

    # print(a1, a2, b1, b2)
    if a1 > b1:
        if b1 < a1 < b2 < a2:
            res.append("YES")
        else:
            res.append("NO")
    else:
        if a1 < b1 < a2 < b2:
            res.append("YES")
        else:
            res.append("NO")

for r in res:
    print(r)
