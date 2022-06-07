#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    args = sys.argv
    argc = len(args)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(args[1])
    b = int(args[3])
    operator = args[2]
    result = 0
    ops = ["+", "-", "*", "/"]
    if operator not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        if operator == "+":
            result = add(a, b)
        elif operator == "-":
            result = sub(a, b)
        elif operator == "*":
            result = mul(a, b)
        else:
            result = div(a, b)

        print("{} {} {} = {}".format(a, operator, b, result))
