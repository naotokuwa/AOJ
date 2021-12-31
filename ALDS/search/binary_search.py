def main():
    n = int(input())
    S = list(map(int, input().split()))
    q = int(input())
    T = list(map(int, input().split()))
    count = 0
    for t in T:
        if binary_search(S, t)>=0:
            count+=1

    print(count)
    

def binary_search(lis, target):
    left = 0
    right = len(lis)

    while left < right:
        mid = (left+right)//2

        if lis[mid] == target:
            return mid
        elif target < lis[mid]:
            right = mid
        else:
            left = mid + 1
    return -1


if __name__ == "__main__":
    main()
