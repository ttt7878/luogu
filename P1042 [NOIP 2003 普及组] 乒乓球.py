import sys

def shuan(text):
    # 11分制
    z = y = 0
    for i in text:
        if (z >= 11 or y >= 11) and abs(z - y) >= 2:
            print(f"{z}:{y}")
            z = y = 0
        if i == 'W':
            z += 1
        elif i == 'L':
            y += 1
        elif i == 'E':
            print(f"{z}:{y}")   # 始终输出当前比分（包括0:0）
            break

    print()  # 空行分隔

    # 21分制
    z = y = 0
    for i in text:
        if (z >= 21 or y >= 21) and abs(z - y) >= 2:
            print(f"{z}:{y}")
            z = y = 0
        if i == 'W':
            z += 1
        elif i == 'L':
            y += 1
        elif i == 'E':
            print(f"{z}:{y}")
            break

def main():
    text = sys.stdin.read()
    shuan(text)

if __name__ == "__main__":
    main()