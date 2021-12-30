from collections import deque

def main():
    d = deque()
    n, q = map(int , input().split())

    for i in range(n):
        name, time = input().split()
        lis = []
        lis.append(name)
        lis.append(int(time))
        d.append(lis)

    time = 0
    while len(d) > 0:
        in_process = d.popleft()
        process_time = min(q, in_process[1])
        in_process[1]-=process_time
        time+=process_time

        if in_process[1] > 0:
            d.append(in_process)
        else:
            print(in_process[0], time)


if __name__ == "__main__":
    main()