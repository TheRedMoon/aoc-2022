#made this harder than neccesary by wanting a timeplapse of the falling sand x.x

def construct_paths_from_content(content):
    lines = content.splitlines()
    paths = []
    for line in lines:
        numbers = line.split("->")
        list = [tuple(map(int, x.strip().split(","))) for x in numbers]
        paths.append(list)
    print(paths)
    return paths

def is_not_stone_or_sand(grid, x, y):
    return grid[y][x] != "#" and grid[y][x] != "o"

def print_grid(grid):
    grid_str = ""
    for row in grid:
        grid_str += ''.join(row) + "\n"
    print(grid_str)

def sim_drop(grid, start_sand, width, height, r1):
    prev_cor = start_sand
    curr_cor = start_sand
    x = curr_cor[0]
    y = curr_cor[1]
    rest = False
    finished = False
    while x <= width and y <= height and not rest:
        grid[y][x] = "o"
        grid[prev_cor[1]][prev_cor[0]] = "."
        prev_cor = curr_cor
        #if falling forever
        if r1:
            if x == 0 or x == width or y==height:
                grid[y][x] = "."
                finished = True
                break
        else:
            #floor is found so restful
            if y == height:
                rest = True

        # check if flow down:
        if is_not_stone_or_sand(grid, x, y + 1):
            curr_cor = (x, y + 1)
        # check if flow down then left
        elif is_not_stone_or_sand(grid, x - 1, y + 1):
            curr_cor = (x - 1, y + 1)

        # check if flow down then right
        elif is_not_stone_or_sand(grid, x + 1, y + 1):
            curr_cor = (x + 1, y + 1)

        if (curr_cor == prev_cor) :
            rest = True
            if curr_cor == start_sand:
                finished = True

        x = curr_cor[0]
        y = curr_cor[1]

    #uncomment this to see a timelapse of the sand!
    return finished, grid

def simulate_sand_flow(grid, start_sand, width, height, r1=True):
    finished = False
    counter = -1
    while not finished:
        counter += 1
        finished, grid = sim_drop(grid, start_sand, width, height, r1)
    if r1:
        print_grid(grid)
        print(f"r1 {counter}")
    else:
        print_grid(grid)
        #+1 ocunter for the start ball that isnt counted
        print(f"r2 {counter+1}")


def r1(width, height, paths):
    grid = [['.' for x in range(width + 1)] for y in range(height + 1)]
    print(f"made a grid of {width_d} by {height}")

    for path in paths:
        for i in range(1, len(path)):
            x1, y1 = path[i - 1]
            x2, y2 = path[i]
            if y1 == y2:
                # horizontal
                # print(f"horizontal {x1},{x2}")
                for i in range(min(x1, x2), max(x1, x2) + 1):
                    grid[y1][i] = "#"

            # If the points are on the same column, draw a vertical line
            elif x1 == x2:
                # vertical
                # print(f"vertical {y1},{y2}")
                for i in range(min(y1, y2), max(y1, y2) + 1):
                    grid[i][x1] = "#"

    start_sand = (500 - min_width, 0)
    grid[start_sand[1]][start_sand[0]] = "+"

    simulate_sand_flow(grid, start_sand, width_d, height)

def r2( height, paths):
    ##r2 njow we can suddenly move horizontal inf. take a range for -5000,5000 to give the sand enough space.
    # wish i could just add a column on the fly but arrays are immutable.

    grid = [['.' for x in range(-5000, 5000)] for y in range(height + 3)]
    print(f"made a grid of {width_d} by {height + 3}")
    for path in paths:
        for i in range(1, len(path)):
            x1, y1 = path[i - 1]
            x2, y2 = path[i]
            if y1 == y2:
                # horizontal
                for i in range(min(x1, x2), max(x1, x2) + 1):
                    grid[y1][i] = "#"

            # If the points are on the same column, draw a vertical line
            elif x1 == x2:
                # vertical
                for i in range(min(y1, y2), max(y1, y2) + 1):
                    grid[i][x1] = "#"
    # add floor
    for i in range(-5000, 5000):
        grid[height + 2][i] = "#"

    start_sand = (500, 0)
    grid[start_sand[1]][start_sand[0]] = "+"
    # print_grid(grid)

    simulate_sand_flow(grid, start_sand, 5000, height + 2, False)

if __name__ == '__main__':
    with open("input.txt") as file:
        content = file.read()

    paths = construct_paths_from_content(content)
    unpacked = [item for path in paths for item in path]
    height = max(unpacked, key=lambda x: x[1])[1]
    min_width = min(unpacked, key=lambda x: x[0])[0]
    width = max(unpacked, key=lambda x: x[0])[0]

    #maybe for optimizing
    width_d = width-min_width

    #make the width scale
    paths_scaled = [list(map(lambda x: (x[0] - min_width, x[1]), path)) for path in paths]

    r1(width_d,height, paths_scaled)
    r2(height,paths)

