"""
B. Symmetric Encoding

Notes:
abcdefghijklmnopqrstuvwxyz

codeforces
cdefors
"""

t = int(input())

for _ in range(t):
    n, s = int(input()), input()

    r = "".join(sorted(set(s)))
    mirror, last = {}, len(r)-1
    for i in range(len(r) // 2 + 1):
        mirror[r[i]] = r[last - i]
        mirror[r[last - i]] = r[i]
    
    newstr = ""
    for c in s:
        newstr += mirror[c]
    
    print(newstr)