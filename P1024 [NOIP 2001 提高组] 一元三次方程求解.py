def shuru():
    a,b,c,d = map(float,input().split())
    return a,b,c,d
def fujia(x2,x1,a,b,c,d):
    f1 = a * x1**3 + b * x1**2 + c * x1 + d
    f2 = a * x2**3 + b * x2**2 + c * x2 + d
    if abs(f1) < 1e-12:
        return x1
    if abs(f2) < 1e-12:
        return x2
    if x2 - x1 < 1e-4:
        return x1 if abs(f1) < abs(f2) else x2
    x0 = (x1 + x2) / 2
    f0 = a * x0**3 + b * x0**2 + c * x0 + d
    if f1 * f0 < 0:
        return fujia(x0,x1,a,b,c,d)
    else:
        return fujia(x2,x0,a,b,c,d)
def shuan(a,b,c,d):
    end = 0.00
    end_list = []
    eps = 1e-7
    for l in range(-100,100):
        x1 = l
        x2 = l + 1.00
        f1 = a * x1**3 + b * x1**2 + c * x1 + d
        f2 = a * x2**3 + b * x2**2 + c * x2 + d
        if abs(f1) < eps:
            end  = x1
            end_list.append(end)
        elif f1 * f2 < 0:
            end = fujia(x2,x1,a,b,c,d)
            end_list.append(end)
    f100 = a * 100**3 + b * 100**2 + c * 100 + d
    if abs(f100) < 1e-12:
        end = 100.00
        end_list.append(end)
    end_list.sort()
    unique = []
    for r in end_list:
        if not unique or abs(r - unique[-1]) > 1e-5:
            unique.append(r)
    return unique
def main():
    a,b,c,d = shuru()
    end = shuan(a,b,c,d)
    print(f"{end[0]:.2f} {end[1]:.2f} {end[2]:.2f}")
if __name__ == "__main__":
    main()