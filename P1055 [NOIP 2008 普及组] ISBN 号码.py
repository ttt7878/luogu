def main():
    s = input().strip()
    t = s.replace("-", "")

    total = 0
    for i in range(9):
        total += int(t[i]) * (i + 1)

    r = total % 11
    if r == 10:
        code = "X"
    else:
        code = str(r)

    if t[9] == code:
        print("Right")
    else:
        print(s[:-1] + code)


if __name__ == "__main__":
    main()