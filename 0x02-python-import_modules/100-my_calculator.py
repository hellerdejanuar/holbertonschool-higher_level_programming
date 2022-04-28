#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1 as calc
    from sys import argv
    argc = len(argv)
    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]

    if op == '+':
        result = calc.add(a, b)
    elif op == '-':
        result = calc.sub(a, b)
    elif op == '*':
        result = calc.mul(a, b)
    elif op == '/':
        result = calc.div(a, b)
    else:
        print("Unknown operator. Available operators +, -, * and /")
        exit(1)

    print(f"{a} {op} {b} = {result}")
    exit(1)
