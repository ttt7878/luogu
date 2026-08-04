def shuru():
    n = int(input())
    return n
def shuan(n):
    x = 1
    while 1:
        sum = (x**2 + x)//2
        if sum >= n:
            break
        x += 1
    x += 1
    if x%2 == 0:
        sum1 = ((x-2)**2 + (x-2))//2
        n1 = n - sum1
        print(f"{x-n1}/{n1}")
    elif x%2 == 1:
        sum2 = ((x-2)**2 + (x-2))//2
        n2 = n - sum2
        print(f"{n2}/{x-n2}")
def main():
    n = shuru()
    shuan(n)
if __name__ == "__main__":
    main()