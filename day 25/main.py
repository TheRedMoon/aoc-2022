import math


def parse_number(x):
    x =  reversed(x)
    digit = []
    for idx, char in enumerate(x):
        if char == "=":
            n = -2
        elif char == "-":
            n = -1
        else:
            n = int(char)
        res = 5**idx * n
        digit.append(res)
    return sum(digit)


def reverse_proces(x):
    found = False
    num = 0
    res = ''
    while not found:
        num += 1
        if 5**num > x:
            break
    remainder = x
    for pos in range(num):
        b = remainder
        div = math.floor(remainder/5)
        remainder = remainder % 5
        print(f"mod 5 in pos {pos} gives as a remainder of {b} {remainder} and a divisor of {div}")
        if remainder == 3:
            div += 1
            res = '=' + res
        elif remainder == 4:
            div += 1
            res = '-' + res
        else:
            res = str(remainder) + res
        remainder = div
    return res


if __name__ == '__main__':
    with open("test.txt") as file:
        content = file.read()
    numbers = [parse_number(x) for x in content.splitlines()]
    res = sum(numbers)
    res =reverse_proces(res)
    print(res)