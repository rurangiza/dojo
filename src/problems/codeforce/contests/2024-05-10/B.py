"""
Codeforces : Round 944 (Div.4)
My First Sorting Problem
"""
t = int(input())

res = []

def mix(string):
    s = [c for c in string]
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            tmp = s[i]
            s[i] = s[i-1]
            s[i-1] = tmp
            break
    return "".join(s)

for i in range(t):
    s = input().strip()
    if len(s) <= 1 or s.count(s[0]) == len(s):
        res.append(["NO"])
    else:
        res.append(["YES", mix(s)])

for r in res:
    print(r[0])
    if r[0] == "YES":
        print(r[1])
