def shuru():
    a,b = map(int,input().split())
    return a,b
def shuanfa(N,M):
    sum1 = 0
    sum = 0
    for i in range(0,N):
        for n in range(i+1,N+1):
            for a in range(0,M):
                for m in range(a+1,M+1):
                    if n-i == m-a:
                        sum += 1
                    else:
                        sum1 += 1
    return sum,sum1

if __name__ == "__main__":
    a,b = shuru()
    c,d = shuanfa(a,b)
    print(c,d)
    
