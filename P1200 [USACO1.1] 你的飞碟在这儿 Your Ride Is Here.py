def shuru():
    hui = input()
    dui = input()
    a = list(hui)
    b = list(dui)
    z = 0
    c = []
    d = []
    for i in range(0,len(a)):
        z = ord(a[i]) - 64
        c.append(z)
    for i in range(0,len(b)):
        z = ord(b[i]) - 64
        d.append(z)
    return c,d
def shuanfa(a,b):
    sum1 = 1
    sum2 = 1
    for i in range(0,len(a)):
        sum1 *= a[i]
    for i in range(0,len(b)):
        sum2 *= b[i]
    if (sum1 % 47) == (sum2 % 47):
        return "GO"
    elif (sum1 % 47) != (sum2 % 47):
        return "STAY"

if __name__ == "__main__":
    a,b = shuru()
    p = shuanfa(a,b)
    print(p)
