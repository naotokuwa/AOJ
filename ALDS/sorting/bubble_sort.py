def bubble_sort(n, lis):
    flag = True
    count = 0
    i = 0
    while flag:
        flag = False

        for j in range(n-1, i, -1):
            if lis[j] < lis[j-1]:
                count+=1
                tmp = lis[j]
                lis[j] = lis[j-1]
                lis[j-1] = tmp
                flag = True
        i+=1
    
    output_array(lis)
    print(count)


def output_array(lis):
    string = ""
    for i in range(len(lis)):
        string+=str(lis[i])
        if i!= len(lis)-1:
            string+=" "
    print(string)

def main():
    n = int(input())
    lis = list(map(int, input().split()))
    bubble_sort(n, lis)


if __name__ == "__main__":
    main()
