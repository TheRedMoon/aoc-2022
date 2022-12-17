import math
import sys
from enum import Enum

shapes = """####

.#.
###
.#.

..#
..#
###

#
#
#
#


##
##
"""

height = 50000
width = 7


class Direction(Enum):
    DOWN = 1
    RIGHT = 2
    LEFT = 3

def print_grid(grid):
    grid_str = ""
    for row in grid:
        grid_str += ''.join(row) + "\n"
    #print(grid_str)

def string_to_coords(s):
    lines = s.split('\n')
    coordinates = []
    x = len(lines) - 1  # start at the last row
    y = 0
    for line in lines:
        for ch in line:
            if ch == '#':
                coordinates.append((x, y))
            y += 1
        x -= 1  # move to the next row up
        y = 0
    return coordinates


def get_highest_point_in_grid(grid):
    lowest_row = len(grid)  # Initialize to len(grid) in case no rows have a #
    for y, row in enumerate(grid):
        if "#" in row:
            lowest_row = y
            #print("Found new lowest row")
            break  # No need to keep looping once we find a row with a #
    return lowest_row


def spawn_rock(grid, shape):
    y = get_highest_point_in_grid(grid) - 4
    x = 2 #spawn 2 from the left
    #print(f"lowest spawn point {x}, {y}")
    coordinates = []
    #print(shape)
    for entry in shape:
        x2,y2 = entry
        new_coord = (x+y2, y-x2)
        #print(f"new coor spawn point {x+y2}, {y-x2}")
        coordinates.append(new_coord)
        grid[new_coord[1]][new_coord[0]] = '@'
    #print("start")
    print_grid(grid)
    return coordinates


def check_if_coor_valid(grid, new_coor):
    x,y = new_coor
    in_grid = 0 <= x < width and 0 <= y < height
    no_rested_rock = False
    if in_grid:
        no_rested_rock = grid[y][x] != "#"
    return no_rested_rock


def move_rock(old_grid, coor_rock, direction):
    new_coordinates = []
    new_grid = old_grid
    for coor in coor_rock:
        x1,y1 = coor

        if direction == Direction.DOWN:
            new_coor = (x1,y1+1)
        elif direction == Direction.LEFT:
            new_coor = (x1-1, y1)
        else:
            new_coor = (x1+1, y1)

        if not check_if_coor_valid(new_grid, new_coor):
            if direction == Direction.DOWN:
                for coor in coor_rock:
                    x,y = coor
                    #rest the rock
                    old_grid[y][x] = "#"
                return old_grid, coor_rock, True
            else:
                return old_grid, coor_rock, False
        new_coordinates.append(new_coor)
        if (x1, y1) not in new_coordinates:
            new_grid[y1][x1] = "."
    for coordinate in new_coordinates:
        #reset old position
        new_grid[coordinate[1]][coordinate[0]] = "@"
    return new_grid, new_coordinates, False


def fall_rock(grid, coor_rock, wind):
    #move one left
    #print(wind)


    if wind == "<":
        grid, coor_rock, rested = move_rock(grid,coor_rock, Direction.LEFT)
    else:
        grid, coor_rock, rested = move_rock(grid, coor_rock, Direction.RIGHT)

    #print("down")
    grid, coor_rock, rested = move_rock(grid,coor_rock, Direction.DOWN)

    return grid, coor_rock, rested


def sim_rock(shape, grid, gust_of_winds, wind_index):
    #gust_of_wind_idx = fallen_rocks % len(gust_of_winds) + 6
    rested = False
    coor_rock = None
    while not rested:
        if coor_rock is None:
            coor_rock = spawn_rock(grid,shape)
        else:
            wind_index = wind_index % len(gust_of_winds)
            wind = gust_of_winds[wind_index]
            grid, coor_rock, rested = fall_rock(grid, coor_rock,wind)
            wind_index += 1
    return wind_index


def get_total_height_cycles(height, grid, height_r1, fallen_rocks, range_f2):
    height_per_cycle = (height - get_highest_point_in_grid(grid)) - height_r1
    amount_of_rocks_cycle = fallen_rocks - 2021
    cycles_to_go = math.floor((range_f2 - fallen_rocks) / amount_of_rocks_cycle)
    fallen_rocks += amount_of_rocks_cycle * cycles_to_go
    total_height_cycles = height_per_cycle * cycles_to_go
    return fallen_rocks, total_height_cycles


def find_pattern(height_per_rock):
    list_of_diff = []
    for x in range(1,len(height_per_rock)):
        prev = height_per_rock[x-1]
        curr = height_per_rock[x]
        diff = curr - prev
        list_of_diff.append(diff)
    return list_of_diff

if __name__ == '__main__':
    with open("test.txt") as file:
        gust_of_winds = file.read() #can use str as char list

    list_of_shapes = [string_to_coords(x) for x in shapes.split("\n\n")]
    list_of_shapes[4] = [(1, 0), (1, 1), (0, 0), (0, 1)] #function does not parse this right, just hardforce it, can't be bothered to check the fucntion for bugs
    #print(list_of_shapes)
    grid = [['.' for j in range(width)] for i in range(height)]
    shape_counter = -1
    wind_index = 0
    grid[7][5] = "S"
    height_r1 = 0
    range_f1 = 2022
    range_f2 = 1000000000000
    pattern = []
    height_per_rock = []
    total_height_cycles = 0
    fallen_rocks = 0
    while fallen_rocks < range_f2:
        shape_counter += 1
        #print(f"{len(shapes)} , {shape_counter}")

        shape_counter = shape_counter % (len(list_of_shapes))

        #print(f"{len(shapes)} , {shape_counter}")
        shape = list_of_shapes[shape_counter]
        wind_index = sim_rock(shape,grid, gust_of_winds, wind_index)
        fallen_rocks += 1

        if fallen_rocks == 2021:
            at_shape = fallen_rocks % 5
            state = [at_shape,wind_index]
            height_r1 = height - get_highest_point_in_grid(grid)
        if fallen_rocks > 2021:
            at_shape = fallen_rocks % 5
            new_state = [at_shape,wind_index]
            #check every 5 fallen stones (so after every set of shapes) if the set of moves is the same we get the same result -> loop
            if state == new_state and total_height_cycles == 0:
                fallen_rocks, total_height_cycles = get_total_height_cycles(height, grid, height_r1, fallen_rocks, range_f2)

    height = height - get_highest_point_in_grid(grid)

    print(f"r1 {height_r1}")
    print(f"r2 {height+total_height_cycles}")










