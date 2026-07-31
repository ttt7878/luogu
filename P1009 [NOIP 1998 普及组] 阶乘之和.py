def shuru():
    n = int(input())
    return n
def shuan(n):
    a = []
    shu = 1
    for i in range(1,n+1):
        shu *= i
        a.append(shu)
    return sum(a)
def main():
    n = shuru()
    end = shuan(n)
    print(end)
if __name__ == "__main__":
    main()