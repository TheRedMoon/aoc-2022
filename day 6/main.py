

def check_if_different(x):
    print(x)
    if len(x) > len(set(x)):
        return False
    return True

char_seen = []


def r(line, number):
    for idx, char in enumerate(line):
        if len(char_seen) > number:
            char_seen.pop(0)
        char_seen.append(char)
        if check_if_different(char_seen) and len(char_seen)>number:
            print(f"index {idx}")
            break

if __name__ == '__main__':
    with open("input.txt") as file:
        lines = [line.rstrip('\n') for line in file]
    line = lines[0]
    r(line,4)
    r(line,14)

