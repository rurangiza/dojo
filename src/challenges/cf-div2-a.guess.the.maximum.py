"""
A. Guess the Maximum

Link: https://codeforces.com/contest/1979/problem/A
"""

def answer():
    n = int(input())
    a = list(map(int, input().split()))
    smallest_max = float('inf')
    L = 0
    for R in range(1, n):
        smallest_max = min(smallest_max, max(a[L:R+1]))
        L += 1
    return smallest_max - 1
    
def main():
    t = int(input())
    for _ in range(t):
        print(answer())

main()
