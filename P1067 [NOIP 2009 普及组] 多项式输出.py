def main():
    n = int(input())
    a = list(map(int,input().split()))
    sum = ""
    for i in range(n+1):
        b = ""
        if a[i] < 0:
            b = "-"
        elif a[i] == 0:
            continue
        elif a[i] > 0 and i != 0:
            b = "+"
        if i == len(a)-2:
            if abs(a[i]) == 1:
                c = f"{b}x" 
                sum = sum + c
                continue
            c = f"{b}{abs(a[i])}x"
            sum = sum + c
            continue
        if i == n:
            c = f"{b}{abs(a[i])}"
            sum = sum + c
            continue
        if abs(a[i]) == 1 and i != n:
            c = f"{b}x^{len(a)-i-1}"
            sum = sum + c
            continue
        c = f"{b}{abs(a[i])}x^{len(a)-i-1}"
        sum = sum + c
    print(sum)
if __name__ == "__main__":
    main()