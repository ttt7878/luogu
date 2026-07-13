def shuru():
    a1 = []
    b1 = []
    N = int(input())
    for i in range(N):
        a,b = map(int,input().split())
        a1.append(a)
        b1.append(b)
    return a1,b1,N
def shuanfa(a,b,n):
    max_sum = 0
    for i in range(n):
        cover = [0] * 1000
        for j in range(n):
            if i == j:
                continue
            start = a[j]
            end = b[j]
            for t in range(start,end):
                cover[t] = 1
        if sum(cover) > max_sum:
            max_sum = sum(cover)
    return max_sum

if __name__ == "__main__":
    a,b,n = shuru()
    c = shuanfa(a,b,n)
    print(c)