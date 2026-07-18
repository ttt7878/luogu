def shuru():
    a = []
    b = []
    n = int(input())
    for i in range(3):
        c,d = map(int,input().split())
        a.append(c)
        b.append(d)
    return n,a,b
def shuanfa(n,quantity,rate):
    sum_quantity = 0
    j = 1
    sum_rate = []
    for i in range(3):
        while 1:
            sum_quantity = j * quantity[i]
            if sum_quantity >= n:
                rate1 = j * rate[i]
                sum_rate.append(rate1)
                j = 1
                break
            j += 1
    return sum_rate
def main():
    n,quantity,rate = shuru()
    sum = shuanfa(n,quantity,rate)
    print(min(sum))
if __name__ == "__main__":
    main()