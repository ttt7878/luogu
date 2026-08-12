def shuan(zhong,hou):
    if not zhong or not hou:
        return ""
    zhong_a = []
    zhong_b = []
    hou_a = []
    hou_b = []
    start = hou[-1]
    k = 0
    for i in zhong:
        if i == start:
            zhong_b = zhong[k+1:]
            break
        zhong_a.append(i)
        k += 1
    hou_a = hou[:len(zhong_a)]
    hou_b = hou[len(zhong_a):-1]
    return start + shuan(zhong_a,hou_a) + shuan(zhong_b,hou_b)
def main():
    zhong = input().strip()
    hou = input().strip()
    print(shuan(zhong,hou))
if __name__ == "__main__":
    main()