"""
B. XOR Sequences

Link: https://codeforces.com/contest/1979/problem/B
"""

def answer():
    x, y = map(int, input().split())
    size = max(x, y)
    xvect = [n+1 ^ x for n in range(size)]
    yvect = [n+1 ^ y for n in range(size)]
    yset = set(yvect)
    longest = 0
    for i in range(len(xvect)):
        cur = xvect[i]
        if cur in yset:
            idx = yvect.index(cur)
            length = i
            while length < size and idx < size and xvect[length] == yvect[idx]:
                length += 1
                idx += 1
            longest = max(longest, length - i)
    return longest

t = int(input())
for _ in range(t):
    print(answer())