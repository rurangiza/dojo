
# maximum number of draws
def solve(p1, p2, p3):
    return min((p1 + p2 + p3) // 2, p1 + p2)

def main():
    t = int(input())
    for _ in range(t):
        p1, p2, p3 = map(int, input().split())
        print(solve(p1, p2, p3))

main()