from typing import List
import re

class Tower():

    def __init__(self, id, crate):
        self.id = id
        self.crates = []
        crate = crate.strip()
        self.crates.append(crate)

    def add_crate(self, crate):
        crate = crate.strip()
        self.crates.append(crate)

    def add_crate_start(self, crate):
        crate = crate.strip()
        self.crates.insert(0, crate)


    def add_crates(self, crates):
        for idx, crate in enumerate(crates):
            self.crates.insert(idx, crate)

    def __str__(self):
        string = ""
        for crate in self.crates:
            string+= crate + "\n"
        string+= str(self.id)
        return string

    def __lt__(self, other):
        return self.id < other.id

towers = []

def has_numbers(inputString):
    return bool(re.search(r'\d', inputString))

def run_move_command(num, source, target):
    print(f'moving {num} crates from {source} to {target}')
    source = tower_exists(int(source))
    target = tower_exists(int(target))
    for i in range(0,int(num)):
        top_crate = source.crates.pop(0)
        print(f'moving crate: {top_crate}')
        target.add_crate_start(top_crate)
    print(f'Source now looks like \n{source}')
    print(f'target now looks like \n{target}')

def run_move_command_r2(num, source, target):
    print(f'moving {num} crates from {source} to {target}')
    source = tower_exists(int(source))
    target = tower_exists(int(target))
    crates = []
    for i in range(0,int(num)):
        top_crate = source.crates.pop(0)
        crates.insert(i,top_crate)
        print(f'moving crate: {top_crate}')
    target.add_crates(crates)
    print(f'Source now looks like \n{source}')
    print(f'target now looks like \n{target}')

def tower_exists(id):
    for tower in towers:
        if tower.id == id:
            return tower
    return None


def add_to_tower(crate, tower_id):
    #print(f'adding crate {crate} to {tower_id}')
    tower = tower_exists(tower_id)
    if tower:
        #print(tower)
        tower.add_crate(crate)
    else:
        tower = Tower(tower_id,crate)
        towers.append(tower)


def get_top_each_tower():
    message = ""
    towers.sort()
    for tower in towers:
        print(tower)
        message += str(tower.crates.pop(0)).replace("[", "").replace("]", "")
    return message


if __name__ == '__main__':
    with open("input.txt") as file:
        lines = [line.rstrip('\n') for line in file]
    for line in lines:
        words = line.split()
        if not words:
            continue

        if words[0] == "move":
            #run_move_command(words[1], words[3], words[5])
            run_move_command_r2(words[1], words[3], words[5])
        else:
            n = 4
            tower_mapped = [line[i:i + n] for i in range(0, len(line), n)]
            for idx, tower in enumerate(tower_mapped):
                if not tower.isspace() and not has_numbers(tower):
                    add_to_tower(tower, int(idx+1))
    print(get_top_each_tower())

        # else:
        #     construct_towers(words)



