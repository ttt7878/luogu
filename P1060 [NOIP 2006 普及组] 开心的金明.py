
def main():
    n,m = map(int,input().split())
    v = []
    p = []
    for _ in range(m):
        a,b = map(int,input().split())
        v.append(a)
        p.append(b)
    end = [0] * (n+1)
    for i in range(len(v)):
        for j in range(n,v[i]-1,-1):
            end[j] = max(end[j],end[j-v[i]] + (v[i]*p[i]))
    print(max(end))
if __name__ == "__main__":
    main()