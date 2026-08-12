def shuru():
    x0,y0 = map(int,input().split())
    return x0,y0
def shuan(x0,y0):
    sum = 0
    chuo = []
    biao = []
    for i in range(x0,y0+1,x0):
        if y0 % i != 0:
            continue
        for j in range(x0,y0+1,x0):
            if y0 % j != 0:
                continue
            flag = True
            for k in range(x0+1,min(i,j)+1):
                if i % k == 0 and j % k == 0:
                    flag = False
            if not flag:
                continue
            for l in range(max(i,j),y0):
                if l % i == 0 and l % j == 0:
                    flag = False
            if flag:
                sum += 1
    return sum
def main():
    x0,y0 = shuru()
    end = shuan(x0,y0)
    print(end)
if __name__ == "__main__":
    main()