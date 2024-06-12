"""
A.Twins
Link: https://codeforces.com/problemset/problem/160/A
"""
def coinsToPick(coins, n):
    tot = sum(coins)
    mine = count = 0
    coins.sort(reverse=True)
    for coin in coins:
        mine += coin
        count += 1
        if mine > tot // 2: break
    return count
    
def main():
    n = int(input())
    coins = list(map(int, input().split()))
    print(coinsToPick(coins, n))

main()