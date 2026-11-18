def main():
    yuan = input().strip()
    jie = input().strip()
    end = input().strip()
    pan = 0
    biao = [0] * 26
    biao2 = [0] * 26
    for i in range(len(yuan)):
        a = ord(yuan[i]) - 65
        b = ord(jie[i]) - 65
        if biao[a] != 0 and jie[i] != biao[a]:
            pan = 1
            break
        if biao2[b] != 0 and yuan[i] != biao2[b]:
            pan = 1
            break
        biao[a] = jie[i]
        biao2[b] = yuan[i]
    if pan == 0:
        if 0 in biao or 0 in biao2:
            pan = 1
    end1 = [0] * len(end)
    if pan == 0:
        for j in range(len(end)):
            b = ord(end[j]) - 65
            end1[j] = biao[b]
        if 0 in end1:
            pan = 1
    if pan == 1:
        print("Failed")
    else:
        print("".join(end1))
if __name__ == "__main__":
    main()