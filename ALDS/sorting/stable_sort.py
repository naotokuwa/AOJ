def bubble_sort(n, lis):
    for i in range(n):
        for j in range(n-1, i, -1):
            if int(lis[j][1]) < int(lis[j-1][1]):
                tmp = lis[j]
                lis[j] = lis[j-1]
                lis[j-1] = tmp

    output_array(lis)
    


def selection_sort(n, lis):
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if int(lis[min_index][1]) > int(lis[j][1]):
                min_index = j
        tmp = lis[min_index]
        lis[min_index] = lis[i]
        lis[i] = tmp
    output_array(lis)
    


def output_array(lis):
    string = ""
    for i in range(len(lis)):
        string+=lis[i]
        if i!= len(lis)-1:
            string+=" "
    print(string)


def judge_stable(bubble_lis, selec_lis):
    for i in range(len(bubble_lis)):
        if bubble_lis[i] != selec_lis[i]:
            print("Not stable")
            exit()
        
    print("Stable")

def main():
    n = int(input())
    lis = list(input().split())
    lis_selec = [lis[i] for i in range(n)]
    bubble_sort(n, lis)
    print("Stable")
    selection_sort(n, lis_selec)
    judge_stable(lis, lis_selec)


if __name__ == "__main__":
    main()
