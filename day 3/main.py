
def convert_to_priority(char):
    if char.isupper():
        char = char.lower()
        priority = (ord(char) - 96) + 26

    else:
        priority = ord(char) - 96

    return priority

if __name__ == '__main__':
    with open("input.txt") as file:
        lines = [line.rstrip('\n') for line in file]

    total_prio = 0
    total_prio_r2 = 0
    lines_found = 0
    group = []
    list_of_groups = []
    for line in lines:
        #could've just used next and iter but too much thinking
        lines_found += 1
        group.append(line)
        if lines_found % 3 == 0:
            list_of_groups.append(group)
            group = []
            lines_found = 0
        half = int(len(line)/2)
        x,y = line[:half], line[half:]
        x = set(x)
        y = set(y)
        res = list(x.intersection(y))[0]
        priority = convert_to_priority(res)
        total_prio += priority

    for group in list_of_groups:
        x,y,z = group
        x = set(x)
        y = set(y)
        z = set(z)
        common_char = list(x.intersection(y, z))[0] #can also use bitwise and set(x) & set(y) & set(z)
        priority = convert_to_priority(common_char)

        total_prio_r2 += priority

    print('priority r1', total_prio)
    print('priority r2', total_prio_r2)
