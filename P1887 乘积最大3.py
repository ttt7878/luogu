import sys

def shuru():
    N, M = map(int, input().split())
    return N, M

def shuanfa(N, M):
    q = N // M
    r = N % M
    ans_list = [str(q)] * (M - r) + [str(q + 1)] * r
    return ' '.join(ans_list)

if __name__ == "__main__":
    N, M = shuru()
    a = shuanfa(N, M)
    sys.stdout.write(a + '\n')