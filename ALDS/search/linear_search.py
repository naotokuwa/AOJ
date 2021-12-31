def mine():
    n = int(input())
    S = list(map(int, input().split()))
    q = int(input())
    T = list(map(int, input().split()))

    set_lis = set()
    for t in T:
        for s in S:
            if t == s:
                set_lis.add(t)
    print(len(set_lis))


def main():
    n = int(input())
    S = list(map(int, input().split()))
    q = int(input())
    T = list(map(int, input().split()))

    count = 0
    for t in T:
        if linear_search(S, t) >=0:
            count+=1
    print(count)


def linear_search(lis, target):
    lis.append(target)
    n = len(lis)
    i = 0

    while lis[i] != target:
        i+=1

    if i == n-1:
        return -1
    else:
        return i

if __name__ == "__main__":
    main()
