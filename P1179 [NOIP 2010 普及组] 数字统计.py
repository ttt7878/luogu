def shuru():
    a = []
    b = []
    xiao,da = map(int,input().split())
    a.append(xiao)
    b.append(da)
    return xiao,da
def shuanfa(x,d):
    i1 = 0
    i2 = 0
    sum = 0
    for i in range(x,d+1):
        i1 = i //10
        i2 = i % 10
        while 1:
            if i1 == 0:
                if i2 == 2:
                    sum += 1
                break
            elif i1 != 0:
                if i2 == 2:
                    sum += 1
            i2 = i1 % 10
            i1 = i1 // 10
            
    return sum



if __name__ == "__main__":
    x,d = shuru()
    g = shuanfa(x,d)
    print(g)

