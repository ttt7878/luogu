def shuru():
    n,x = map(int,input().split())
    return n,x
def shuanfa(n,x):
    sum = 0
    for i in range(1,n+1):
        while i > 0:
            a = i % 10
            if a == x:
                sum += 1
            i = i // 10
    return sum
def main():
    n,x = shuru()
    a = shuanfa(n,x)
    print(a)
if __name__ == "__main__":
    main()