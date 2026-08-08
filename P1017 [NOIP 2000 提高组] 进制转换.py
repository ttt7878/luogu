def zuan(c):
    if 0 <= c <= 9:
        return chr(ord('0') + c)
    else:
        return chr(ord('A') + c -10)
def shuan(n,r):
    end = []
    yu = 0
    zheng = 0
    n1 = n
    while n1 != 0:
        yu = n1 % r
        zheng = n1 // r
        if yu < 0:
            if r > 0:
                yu = n1 % r + abs(r)
                zheng = n1 // r - 1
            else:
                yu = n1 % r + abs(r)
                zheng = n1 // r + 1
        end.append(zuan(yu))
        n1 = zheng
    return ''.join(end[::-1])
def main():
    n,r = map(int,input().split())
    end = shuan(n,r)
    print(f"{n}={end}(base{r})")
if __name__ == "__main__":
    main() 