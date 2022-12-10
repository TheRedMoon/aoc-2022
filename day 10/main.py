
def run_instr(cycle, r1, value):
    cycle += 1
    if ((cycle + 20) % 40 == 0 or cycle == 20) and cycle < 240:
        to_add = cycle * value
        print(f"Cycle {cycle} vs to add {value} vs adding {to_add} vs total rn {r1}")
        r1 += to_add
    return cycle, r1, value

def run_instr_r2(cycle, res_r2, value):
    mod = cycle % 40
    #only one row forgot to do mod cycle 40 for every row
    if mod == cycle or mod == value-1 or mod == value + 1:
        res_r2 += "#"
    else:
        res_r2 += "."
    cycle += 1
    #40 chars done new line
    if cycle % 40 == 0:
        res_r2 += "\n"

    return cycle, res_r2, value

def r1(lines):
    cycle = 0
    res = 0
    x = 1
    for line in lines:
        words = line.split()
        if words[0] == "noop":
            cycle, res, x = run_instr(cycle, res, x)
        else:
            num = int(words[1])
            cycle, res, x = run_instr(cycle, res, x)
            cycle, res, x = run_instr(cycle, res, x)
            x += num

    return res

def r2(lines):
    cycle = 0
    res = ""
    x = 1
    for line in lines:
        words = line.split()
        if words[0] == "noop":
            cycle, res, x = run_instr_r2(cycle, res, x)
        else:
            num = int(words[1])
            cycle, res, x = run_instr_r2(cycle, res, x)
            cycle, res, x = run_instr_r2(cycle, res, x)
            x += num
    return res

if __name__ == '__main__':
    with open("input.txt") as file:
        lines = [line.rstrip('\n') for line in file]

    r1_res = r1(lines)
    r2_res = r2(lines)
    print(f"R1 result {r1_res}")
    print(f"{r2_res}")
