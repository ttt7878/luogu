def main():
    n = int(input())
    if n == 1:
        print(1)
        return 
    end = [0]*(n+1)
    end[1] = 1
    for i in range(2,n+1):
        totel = 1
        for j in range(1,i // 2 + 1):
            totel += end[j]
        end[i] = totel
    print(end[n])
if __name__ == "__main__":
    main()