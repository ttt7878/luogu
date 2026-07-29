def shuru():
    date = []
    n = int(input())
    for _ in range(n):
        a,b,c,d = map(int,input().split())
        t = (a,b,c,d)
        date.append(t)
    x,y = map(int,input().split())
    f = (x,y)
    return n,date,f
def shuanfa(n,date,f):
    end = -1
    for i in range(n):
        if f[0] >= date[i][0] and f[0] <= date[i][0] + date[i][2] and f[1] >= date[i][1] and f[1] <= date[i][1] + date[i][3]:
            end = i + 1
    return end
def main():
    n,date,f = shuru()
    end = shuanfa(n,date,f)
    print(end)
if __name__ == "__main__":
    main()