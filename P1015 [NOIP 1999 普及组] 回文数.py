def ten(c):
    if '0' <= c <= '9':
        return ord(c) - ord("0")
    else:
        return ord(c) - ord("A") + 10
def retu(d):
    if 0 <= d <= 9:
        return chr(ord("0")+d)
    else:
        return chr(ord("A")+ d - 10)
def add_shuan(a,b,n):
    end = []
    carry = 0
    i,j = len(a)-1,len(b)-1
    while i >= 0 or j >= 0 or carry:
        va = ten(a[i]) if i >= 0 else 0
        vb = ten(b[j]) if j >= 0 else 0
        s = va + vb + carry
        carry = s // n
        end.append(retu(s%n))
        i -= 1
        j -= 1
    return ''.join(reversed(end)) 
def main():
    N = int(input().strip())
    M = input().strip()
    if M == M[::-1]:
        print("STEP=0")
        return
    for i in range(1,31):
        rev = M[::-1]
        M = add_shuan(M,rev,N)
        if M == M[::-1]:
            print(f"STEP={i}")
            return
    print("Impossible!")
if __name__ == "__main__":
    main()