north = [(-1, 0), (-1, 1), (-1, -1)]
south = [(1, 0), (1, 1), (1, -1)]
west =  [(0,-1), (-1, -1), (1, -1)]
east = [(0, 1), (-1, 1), (1, 1)]

def construct_grid(content):
    lines = content.splitlines()
    elf_coords = set()
    for x,line in enumerate(lines):
       for y,char in enumerate(line):
           if char == '#':
            elf_coords.add((x,y))
    return elf_coords


def determine_suggestion(elf, elfs, directions):
    #check if in surrounding there is another elf:
    neightbours = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    elfs_neigh = [(elf[0] + x, elf[1] + y) for x, y in neightbours]
    if any(coord in elfs for coord in elfs_neigh):
        for dir_nb in directions:
            set = [(elf[0] + x, elf[1] + y) for x, y in dir_nb]
            if not any(coord in elfs for coord in set):
                return dir_nb[0]
        return (0,0)
    else:
        return (0,0)


def check_if_dest_unique(dest, suggestions):
    counter = 0
    for value in suggestions.values():
        if value == dest:
            counter += 1
    return counter < 2


def get_retangle(elf_coords):
    x_max = max(elf_coords, key=lambda x: x[0])[0]
    y_max = max(elf_coords, key=lambda y: y[1])[1]
    x_min = min(elf_coords, key=lambda x: x[0])[0]
    y_min = min(elf_coords, key=lambda y: y[1])[1]
    x = x_max + abs(x_min)
    y = y_max + abs(y_min)
    return x+1,y+1

if __name__ == '__main__':
    with open("input.txt") as file:
        content = file.read() #can use str as char list

    elf_coords = construct_grid(content)
    directions = [north, south, west, east]
    final_round = 0
    for round in range(2000):
        suggestions = {}
        nr_moved = 0
        for elf in elf_coords:
            suggestion = determine_suggestion(elf, elf_coords, directions)
            suggestions[elf] = (elf[0] + suggestion[0], elf[1] + suggestion[1])
        for elf, dest in suggestions.items():
            if elf == dest:
                continue
            if check_if_dest_unique(dest, suggestions):
                elf_coords.remove(elf)
                elf_coords.add(dest)
                nr_moved += 1

        directions = directions[1:] + directions[:1]
        print(round, nr_moved)
        if nr_moved == 0:
            final_round = round+1
            break

    x,y = get_retangle(elf_coords) #11 VS 14 should it be
    size = x * y
    empty_size = size - len(elf_coords)

    print(f"R1: {empty_size}")

    print(f"R2 {final_round}")
