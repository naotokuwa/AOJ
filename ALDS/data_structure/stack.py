def main():
    stack = []

    operands = list(input().split())
    
    for operand in operands:
        if operand == "+":
            left = stack.pop()
            right = stack.pop()
            num = int(left) + int(right)
            stack.append(num)
        elif operand == "-":
            left = stack.pop()
            right = stack.pop()
            num = int(right) - int(left)
            stack.append(num)
        
        elif operand == "*":
            left = stack.pop()
            right = stack.pop()
            num = int(left) * int(right)
            stack.append(num)
        else:
            stack.append(operand)

    print(stack[0])



if __name__ == "__main__":
    main()
