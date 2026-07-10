def shuru():
    a, b = map(int, input().split())
    return a, b

def shuanfa(a, b):
    cnt = [0] * 10
    for i in range(a, b + 1):
        x = i
        while x:
            cnt[x % 10] += 1
            x //= 10
    return cnt

if __name__ == "__main__":
    a, b = shuru()
    c = shuanfa(a, b)
    print(' '.join(map(str, c)))