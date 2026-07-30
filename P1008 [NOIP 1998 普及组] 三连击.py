def main():
    t = (1,2,3,4,5,6,7,8,9)
    for i in range(100,334):
        shu = [
            i % 10, (i // 10) % 10, i // 100,
            (i * 2) % 10, ((i * 2) // 10) % 10, (i * 2) // 100,
            (i * 3) % 10, ((i * 3) // 10) % 10, (i * 3) // 100
        ]
        if tuple(sorted(shu)) == t:
            print(i,2*i,3*i)       
if __name__ == "__main__":
    main()