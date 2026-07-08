def shuru():
    a = int(input())
    return a
def shuanfa(a):
    b = []
    d = 0
    if a > 0:
        while a > 0:
            shuc = a % 10
            b.append(shuc)
            a = a // 10
        for i in range(1,len(b)+1):
            d += b[i-1]*10**(len(b)-i)
        return d
    elif a < 0:
        e = -a
        while e > 0:
            shuc = e % 10
            b.append(shuc)
            e = e // 10
        for i in range(1,len(b)+1):
            d += b[i-1]*10**(len(b)-i)
        return -d
    else:
        return 0

if __name__ == "__main__":
    a = shuru()
    b = shuanfa(a)
    print(b)

