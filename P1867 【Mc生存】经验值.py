def shuru():
    n = int(input())
    lose = []
    experience = []
    for i in range(n):
        a,b = input().split()
        a = float(a)
        b = int(b)
        lose.append(a)
        experience.append(b)
    return lose,experience
def shuanfa(lose,experience):
    sum = 10
    sum1 = 0
    Level = 0
    end = []
    for i in range(len(lose)):
        sum = sum - lose[i]
        if sum > 10:
            sum = 10
        if sum > 0:
            sum1 = sum1 + experience[i]
        elif sum <= 0:
            break
    while 1:
        Level_sum = (2**Level)-1
        if Level_sum > sum1:
            b = sum1 - ((2**(Level-1))-1)
            a = Level - 1
            end.append(a)
            end.append(b)
            break
        elif Level_sum == sum1:
            a = Level
            b = 0
            end.append(a)
            end.append(b)
            break
        Level += 1
    return end
if __name__ == "__main__":
    lose,experience = shuru()
    a = shuanfa(lose,experience)
    print(a[0],a[1])
