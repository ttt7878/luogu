def sr():
    a = []
    for i in range(12):
        ys = int(input())
        a.append(ys)
    return a
def cc(b):
    c = []
    sum = 0
    sum2 = 0
    sum3 = 0      #sum是每次总剩余钱减去百位数的剩余钱。
                    #sum2表示每次被减去的百位。
                    # sum3表示存储在妈妈那里的钱。
    for i in range(12):
        sum2 = 0
        sum1 = sum + 300 - b[i]
        if sum1 >= 100:
            sum2 = (sum1 // 100) *100
            sum = sum1 - sum2
        elif sum1 < 0:
            c.append(-(i+1))
        else:
            sum = sum1
            
        sum3 += sum2
    if len(c) == 0:
        return int(sum3*1.2 + sum)
    else:
        return c[0]

if __name__ == "__main__":
    b = []
    b = sr()
    c = cc(b)
    print(c)
    
