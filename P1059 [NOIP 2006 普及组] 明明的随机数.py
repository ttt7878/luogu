
def main():
    N = int(input())
    a1 = list(map(int,input().split()))
    a1 = list(set(a1))
    a1 = sorted(a1)
    print(len(a1))
    print(' '.join(map(str,a1)))
if __name__ == "__main__":
    main()