import math
def shuan(N,k,N_list):
    def shu(num):
        if num < 2:
            return False
        for i in range(2,int(math.isqrt(num))+1):
            if num % i == 0:
                return False
        return True
    ans = 0
    def dig(start,cnt,total):
        nonlocal ans
        if cnt == k:
            if shu(total):
                ans += 1
            return
        if start + (k - cnt) > N:
            return
        for i in range(start,N):
            dig(i+1,cnt+1,total+N_list[i])
    dig(0,0,0)
    print(ans)
def main():
    N,k = map(int,input().split())
    N_list = list(map(int,input().split()))
    shuan(N,k,N_list)
if __name__ == "__main__":
    main()