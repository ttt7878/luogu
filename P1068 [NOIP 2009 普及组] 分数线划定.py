def main():
    n,m = map(int,input().split())
    k1 = []
    s1 = []
    for _ in range(n):
        k,s = map(int,input().split())
        k1.append(k)
        s1.append(s)
    sum2 = sorted(zip(k1,s1),key= lambda p:(-p[1],p[0]))
    k3,s3 = zip(*sum2)
    k3 = list(k3)
    s3 = list(s3)
    a = (m * 3) // 2
    b = a-1
    while 1:
        if b == n:
            break
        if s3[b] != s3[a-1]:
            break
        b += 1
    print(s3[a-1],b)
    for i in range(b):
        print(k3[i],s3[i])
if __name__ == "__main__":
    main()