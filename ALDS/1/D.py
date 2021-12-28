def first():
    n = int(input())
    lis = [int(input()) for _ in range(n)]
    max_dif = -1 * (10 **10)
    min_val = lis[0]

    for i in range(1, n):
        max_dif = max(max_dif, lis[i]-min_val)
        min_val = min(min_val, lis[i])
    print(max_dif)




if __name__ == "__main__":
    first()
