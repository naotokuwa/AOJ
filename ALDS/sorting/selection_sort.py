def selection_sort(n, lis):
    count = 0
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if lis[j] < lis[min_index]:
                min_index = j
        if min_index != i:
            tmp = lis[min_index]
            lis[min_index] = lis[i]
            lis[i] = tmp
            count+=1
    
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
    selection_sort(n, lis)



if __name__ == "__main__":
    main()
