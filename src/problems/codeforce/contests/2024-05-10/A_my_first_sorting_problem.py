"""
Codeforces : Round 944 (Div.4)
My First Sorting Problem
"""
gi = lambda: list(map(int, input().strip().split()))
res = []

t = int(input())
for i in range(t):
    x, y = gi()
    res.append(f'{min(x, y)} {max(x, y)}')

for r in res:
    print(r)