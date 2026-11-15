def main():
    k, n = map(int, input().split())

    ans = 0
    base = 1

    while n:
        if n & 1:
            ans += base
        base *= k
        n >>= 1

    print(ans)


if __name__ == "__main__":
    main()