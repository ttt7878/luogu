def shuru():
    kong_x = []
    kong_y = []
    n, m, ma_x, ma_y = map(int, input().split())
    kong_x.append(ma_x)
    kong_y.append(ma_y)
    sum = 3
    for i in range(1, 3):
        a1 = ma_x - i
        b1 = ma_y - (sum - i)
        kong_x.append(a1)
        kong_y.append(b1)
        b2 = ma_y + (sum - i)
        kong_x.append(a1)
        kong_y.append(b2)
        a2 = ma_x + i
        kong_x.append(a2)
        kong_y.append(b1)
        kong_x.append(a2)
        kong_y.append(b2)
    return kong_x, kong_y, n, m


def shuanfa(kong_x, kong_y, n, m):
    blocked = set()
    for x, y in zip(kong_x, kong_y):
        if 0 <= x <= n and 0 <= y <= m:
            blocked.add((x, y))
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    if (0, 0) not in blocked:
        dp[0][0] = 1
    for i in range(n + 1):
        for j in range(m + 1):
            if (i, j) in blocked:
                dp[i][j] = 0
                continue
            if i == 0 and j == 0:
                continue
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
    return dp[n][m]


def main():
    kong_x, kong_y, n, m = shuru()
    end = shuanfa(kong_x, kong_y, n, m)
    print(end)


if __name__ == "__main__":
    main()