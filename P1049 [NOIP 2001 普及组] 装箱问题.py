def main():
    v = int(input())
    V = [0] * (v+1)
    n = int(input())
    for _ in range(n):
        a = int(input())
        for i in range(v,a-1,-1):
            V[i] = max(V[i],V[i-a]+a)
    print(v - max(V))
if __name__ == "__main__":
    main()