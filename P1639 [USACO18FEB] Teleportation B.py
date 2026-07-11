def shuru():
    a1 = []
    a,b,c,d = map(int,input().split())
    a1.append(a)
    a1.append(b)
    a1.append(c)
    a1.append(d)
    return a1
def shuanfa(a1):
    return min(abs(a1[1]-a1[0]),abs(a1[0]-a1[2])+abs(a1[3]-a1[1]),abs(a1[0]-a1[3])+abs(a1[2]-a1[1]))
if __name__ == "__main__":
    a1 = shuru()
    a2 = shuanfa(a1)
    print(a2)
