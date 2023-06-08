#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

        calc = {"+": add, "-": sub, "*": mul, "/": div}
        if sys.arv[2] not in list(calc.keys()):
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)

        sys.argv[1] = a
        sys.argv[3] = b
        print("{} {} {} = {}".format(a, sys.argv[2], b, calc[sys.argv[2]](a, b)))
