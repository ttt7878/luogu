def shuru():
    a1 = []
    b1 = []
    t = int(input())
    for i in range(t):
        a, b = map(int, input().split())
        a1.append(a)
        b1.append(b)
    return t, a1, b1

def shuanfa(t, n, k):
    d = []
    for i in range(t):
        min_need = k[i] * (k[i] + 1) // 2
        if n[i] >= min_need:
            d.append("Yes")
        else:
            d.append("No")
    return d

if __name__ == "__main__":
    t, n, k = shuru()
    c = shuanfa(t, n, k)
    for i in range(len(c)):
        print(c[i])