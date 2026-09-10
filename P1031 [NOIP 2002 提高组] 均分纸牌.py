def shuru():
    N = int(input())
    nums = list(map(int,input().split()))
    return N,nums
def shuan(N,nums):
    end = sum(nums) // N
    a = 0
    b = 0
    for i in range(N-1):
        a += nums[i] - end
        if a != 0:
            b += 1
    return b
def main():
    N,nums = shuru()
    end = shuan(N,nums)
    print(end)
if __name__ == "__main__":
    main()