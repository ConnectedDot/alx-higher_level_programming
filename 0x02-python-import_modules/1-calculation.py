#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def main():
    """Print the sum, difference, product and quotient of 10 and 5."""
    a = 10
    b = 5

    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {sub(a, b)}")
    print(f"{a} * {b} = {mul(a, b)}")
    print(f"{a} / {b} = {div(a, b)}")


if __name__ == "__main__":
    main()
