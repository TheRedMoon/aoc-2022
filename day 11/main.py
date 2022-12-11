
import math
from collections import defaultdict


def parse_monkey(monkey):
    items = list(map(int,monkey[1][18:].split(',')))
    operation = monkey[2][23:].split(" ")
    test = int(monkey[3][21:])
    condition_t = int(monkey[4][29:])
    condition_f = int(monkey[5][30:])

    monkey = {
        "items": items,
        "op": operation,
        "test": test,
        "con":
            {True: condition_t, False: condition_f}}
    return monkey


def eval_worry(item, op, testmod):
    if testmod == 0:
        if op[0] == "*":
            if op[1] == "old":
                return math.floor((item * item) / 3)
            return math.floor((item * int(op[1])) / 3)
        else:
            if op[1] == "old":
                return math.floor((item * item) / 3)
            return math.floor((item + int(op[1])) / 3)
    else:
        if op[0] == "*":
            if op[1] == "old":
                return math.floor((item * item) % testmod)
            return math.floor((item * int(op[1])) % testmod)
        else:
            if op[1] == "old":
                return math.floor((item * item) % testmod)
            return math.floor((item + int(op[1])) % testmod)


def eval_test(worry, test):
    if worry % test == 0:
        return True
    return False


def r(monkeys, testmod=0):
    inspected = defaultdict(int)
    if testmod == 0:
        rang = range(20)
    else:
        rang = range(10000)
    for i in rang:
        for idx,monkey in enumerate(monkeys):
            items = monkey["items"]
            for item in items:
                inspected[idx] += 1
                op = monkey["op"]
                test = monkey["test"]
                worry = eval_worry(item, op, testmod)
                test = eval_test(worry,test)
                if test:
                    con = monkey["con"][True]
                else:
                    con = monkey["con"][False]

                #print(f" Monkey with id {idx} Throw to monkey {con} with worry level {worry}")
                monkeys[con]["items"].append(worry)
            monkey["items"] = []
    sorted_inspected = sorted(inspected.values(), reverse=True)
    res = sorted_inspected[0] * sorted_inspected[1]
    return res

if __name__ == '__main__':
    with open("input.txt") as file:
        lines = file.read().split("\n\n")
        monkeys_f = [line.split('\n') for line in lines]
    monkeys = []
    for m in monkeys_f:
        monkeys.append(parse_monkey(m))
    test_mod = math.prod([x["test"] for x in monkeys])
    print(f"R1 {r(monkeys)}") #58322
    print(f"R2 {r(monkeys, test_mod)}") #13937702909
