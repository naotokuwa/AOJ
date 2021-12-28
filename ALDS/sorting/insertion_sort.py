def insersion_sort(n, lis):
    output_array(lis)
    
    for i in range(1, n):
        
        v = lis[i]
        j = i-1

        while(j>=0 and lis[j]>v):
            lis[j+1] = lis[j]
            j-=1
        lis[j+1] = v

        output_array(lis)

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
    insersion_sort(n, lis)


if __name__ == '__main__':
    main()
