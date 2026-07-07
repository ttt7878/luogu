def shuru():
    a = []
    b = []
    x,y= map(int,input().split())
    a.append(x)
    b.append(y)
    return a,b
def shuanfa(n,k):
    a = n
    b = k
    sum = 0
    sum1 = 0
    while 1:
        sum1 = a - b
        if sum1 >= 0:
            sum += b
            a = sum1 + 1
        else:
            return sum + a

if __name__ == "__main__":
    n,k = shuru()
    sum = shuanfa(n[0],k[0])
    print (sum)

