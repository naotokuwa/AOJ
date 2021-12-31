def main():
    n = int(input())
    commads = [list(input().split()) for _ in range(n)]
    N = set()

    for command in commads:
        if command[0] == "find":
            if command[1] in N:
                print("yes")
            else:
                print("no")
        else:
            N.add(command[1])

if __name__ == "__main__":
    main()
