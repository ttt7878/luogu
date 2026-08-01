import sys

def solve(n):
    if n == 0:
        return ""
    exp = 0
    while (1 << (exp + 1)) <= n:
        exp += 1

    if exp == 0:
        term = "2(0)"
    elif exp == 1:
        term = "2"
    else:
        term = "2(" + solve(exp) + ")"

    rest = n - (1 << exp)
    if rest == 0:
        return term
    else:
        return term + "+" + solve(rest)

def main():
    n = int(sys.stdin.readline().strip())
    print(solve(n))

if __name__ == "__main__":
    main()