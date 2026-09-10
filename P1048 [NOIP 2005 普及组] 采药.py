def main():
    T,M = map(int,input().split())
    dp = [0] * (T+1)
    for _ in range(M):
        t,m = map(int,input().split())
        for i in range(T,t-1,-1):
            dp[i] = max(dp[i],dp[i-t] + m)
    print(dp[T])
if __name__ == "__main__":
    main()