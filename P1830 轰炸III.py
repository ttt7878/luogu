def shuru():
    zs = []
    yx = []
    y1 = []
    y2 = []
    n,m,x,y = map(int,input().split())
    for i in range(x):
        a,b,e,f = map(int,input().split())
        zs.append(a)
        yx.append(b)
        zs.append(e)
        yx.append(f)
    for i in range(y):
        c,d = map(int,input().split())
        y1.append(c)
        y2.append(d)
    return zs,yx,y1,y2
def shuanfa(zs,yx,y1,y2):
    k = 1
    sum1 = 0
    sum2 = 0
    sum_frequency = []
    sum_end = []
    for j in range(len(y1)):
        for i in range(1,len(zs)+1):
            if k % 2 == 0:
                if (y1[j] >= zs[i-2]) and (y1[j] <= zs[i-1]) and (y2[j] >= yx[i-2]) and (y2[j] <= yx[i-1]):
                    sum1 += 1
                    sum2 = i // 2
            else:
                pass
            k += 1
        sum_frequency.append(sum1)
        sum_end.append(sum2)
        sum1 = 0
    return sum_frequency,sum_end
if __name__ == "__main__":
    zs,yx,y1,y2 = shuru()
    a,b = shuanfa(zs,yx,y1,y2)
    for i in range(len(y1)):
        if a[i] != 0:
            print("Y",a[i],b[i])
        else:
            print("N")
