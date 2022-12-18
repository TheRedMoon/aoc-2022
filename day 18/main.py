import collections


def create_cubes(content):
    cubes  = []
    for line in content.splitlines():
        coor = [int(x) for x in line.split(',')]
        cube = tuple(coor)
        cubes.append(cube)
    return set(cubes)

def get_new_coords(dir,cube):
    new_coords = tuple([pair[0] + pair[1] for pair in zip(dir, cube)])
    return new_coords

def cal_sides(dirs, sides):
    for dir in dirs:
        new_coords = get_new_coords(dir,cube)
        if new_coords in cubes:
            sides -= 1
    return sides

def get_sides_every_dir(cube, cubes):
    sides = 6 # cube has 6 sides
    #diff are 1 apart cause every cube is 1x1x1
    zdif = [(0, 0, 1),(0, 0, -1)]
    ydif = [(0, 1, 0),(0, -1, 0)]
    xdif = [(-1, 0, 0),(1, 0, 0)]
    sides = cal_sides(zdif,sides)
    sides = cal_sides(ydif,sides)
    sides = cal_sides(xdif,sides)
    return sides


def bfs(cubes):
    #start at min coordinates (probably 0,0,0)
    #in hindsight it was not. The test is 0,0,0 input is not.
    min_value = (min(t[0] for t in cubes)-1,min(t[1] for t in cubes)-1,min(t[2] for t in cubes)-1)
    max_value = (max(t[0] for t in cubes)+1,max(t[1] for t in cubes)+1,max(t[2] for t in cubes)+1)
    x_max, y_max, z_max = max_value
    x_min, y_min, z_min = min_value
    queue = collections.deque([[min_value]])
    dirs = [(0, 0, 1),(0, 0, -1),(0, 1, 0),(0, -1, 0),(-1, 0, 0),(1, 0, 0)]
    seen = set()
    found_cubes = 0
    while queue:
        coordinate = queue.popleft()[0]
        if coordinate not in seen:
            seen.add(coordinate)
        else:
            continue

        for dir in dirs:
            x,y,z = get_new_coords(dir,coordinate)
            lies_within_bounds_x = x_min <= x <= x_max
            lies_within_bounds_y = y_min <= y <= y_max
            lies_within_bounds_z = z_min <= z <= z_max
            lies_within_bounds = lies_within_bounds_x and lies_within_bounds_y and lies_within_bounds_z
            #check if lies within bounds and if new coord is not a cube:
            if (x,y,z) not in cubes and lies_within_bounds:
                #pocket of air can move here
                queue.append([(x,y,z)])
            elif (x,y,z) in cubes and lies_within_bounds:
                #count every side we encounter
                found_cubes += 1
    return found_cubes

if __name__ == '__main__':
    with open("input.txt") as file:
        content = file.read() #can use str as char list

    sides = 0
    cubes = create_cubes(content)
    for cube in cubes:
        sides += get_sides_every_dir(cube, cubes)
    print(f"r1 {sides}")

    found = bfs(cubes)
    print(f"r2 {found}")
