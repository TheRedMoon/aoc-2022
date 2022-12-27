import sys
from collections import deque
import time


dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (0,0)]

def construct_grid(content):
    coords = []
    blizard_set = set()
    wall_set = set()
    lines = content.splitlines()
    height = len(lines)-1
    id = 0
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if y == 0 and char == ".":
                coords.append((x, y, "E"))
                width = len(line) -1
            elif y == len(lines)-1 and char == ".":
                coords.append((x, y, "G"))
            elif char == ">" or char == "^" or char == "<" or char == "v":
                blizard_set.add((x,y,char))
                id += 1
            elif char == "#":
                wall_set.add((x,y))
            else:
                coords.append((x,y,char))

    return wall_set, blizard_set, coords, height, width


def get_new_coords(dir,coordinates, start):
    if coordinates == start and dir == (0,0):
        dir = dirs[1]

    new_coords = tuple([pair[0] + pair[1] for pair in zip(dir, coordinates)])
    return new_coords


def get_new_blizzard_coords(coor, dir, walls, height, width):
    #print(f"dir {dir} vs coor {coor}")
    new_coords = tuple([pair[0] + pair[1] for pair in zip(dir, coor)])
    #print("new coords" , new_coords)
    if new_coords not in walls:
        x_new,y_new=new_coords
        return (x_new,y_new)
    else:
        #move to the otherside of the map
        x, y = coor
        if dir == (0, 1):
            # down so we appear up
            return (x,1)
        elif dir == (0, -1):
            #up so we appear down
            return (x,height-1)
        elif dir == (1, 0):
            #right so we appear left
            return (1,y)
        elif dir == (-1, 0):
            #left so we appear right
            return (width-1,y)

def char_to_dir(char):
    if char == ">":
        dir = dirs[2]
    elif char == "^":
        dir = dirs[1]

    elif char == "<":
        dir = dirs[3]
    elif char == "v":
        dir = dirs[0]
    else:
        print('gert')
        dir = dirs[0]
    return dir

def dir_to_char(dir):
    if dir == dirs[2]:
        char = ">"
    elif dir == dirs[1]:
        char = "^"
    elif dir == dirs[3]:
        char = "<"
    elif dir == dirs[0]:
        char = "v"
    else:
        char = "x"
    return char

def update_blizzards(blizzards, height, width):
    #print(f"blizzard parameters {height}, {width}, {blizzards}")
    temp_blizzard = set()
    for x,y,char in blizzards:
        dir = char_to_dir(char)
        x1,y1 = get_new_blizzard_coords((x,y), dir, walls, height, width)
        #print(f"old coor {(x,y)} vs new coor {(x1,y1)}")
        temp_blizzard.add((x1,y1,char))

    return temp_blizzard

def is_adjacent(point, other_point):
    x, y = point
    other_x, other_y = other_point
    if (other_x, other_y) in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
        return True
    return False


def bfs(start, end, walls, blizzards, height, width):
    s1,s2 = start
    blizzards_dict = {}
    blizzards_dict[0] = blizzards
    queue = deque([[(s1,s2, 1)]])
    visited = set()
    #visited.add(start)
    rotation = (height-1) * (width -1)
    queue_run = 0
    while queue:
        item = queue.popleft()[0]#first had .pop which caused this function to load forever instead of ~2 min
        queue_run +=1
        x, y, t = item
        #print(f"queue size {len(queue)}")
        if t%rotation not in blizzards_dict.keys():
            state_blizzards = update_blizzards(blizzards_dict[t-1], height, width)
            blizzards_dict[t%rotation] = state_blizzards
        else:
            state_blizzards = blizzards_dict[t%rotation]

        for dir in dirs:
            x1, y1 = get_new_coords(dir, (x,y), start)
            if is_adjacent(end, (x, y)):
                print("found!!!")
                return t
            # check if can move
            no_ids = [(a, b) for a, b, _ in state_blizzards]
            not_in_ids = (x1, y1) not in no_ids
            not_in_walls = (x1, y1) not in walls
            not_in_visited = (x1, y1, t + 1) not in visited

            if not_in_walls and not_in_ids and not_in_visited:
                visited.add((x1, y1, t + 1))
                queue.append([(x1, y1, t + 1)])


if __name__ == '__main__':
    with open("input.txt") as file:
        content = file.read() #can use str as char list
    walls, blizzards, coords, height,width = construct_grid(content)


    x_start,y_start,_ = [t for t in coords if t[2] == "E"][0]


    #add wall above start:
    walls.add((x_start,y_start-1))

    x_end,y_end,_ = [t for t in coords if t[2] == "G"][0]
    print(x_end,y_end)
    number = bfs((x_start,y_start), (x_end,y_end), walls, blizzards, height, width)
    print(f"round 1: {number}" )
    #test blizzard function:
    # round 10

