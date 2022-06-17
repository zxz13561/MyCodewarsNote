def count_change(money, coins):
    dp = [0] * (money + 1)
    dp[0] = 1
    for c in coins:
        for a in range(1, money + 1):
            if a - c >= 0:
                print(c, a, a - c)
                dp[a] += dp[a - c]
    return dp[money]


if __name__ == '__main__':
    data = [10, [2, 3, 5]]
    print(count_change(data[0], data[1]))
