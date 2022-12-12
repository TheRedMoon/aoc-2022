import collections

def get_adjecent(x, y, coordinates):
    right = coordinates.get((x + 1, y))
    left = coordinates.get((x - 1, y))
    up = coordinates.get((x, y + 1))
    down = coordinates.get((x, y - 1))
    values = [(a, b, c) for a, b, c in ((x + 1, y, right), (x - 1, y, left), (x, y + 1, up), (x, y - 1, down)) if c is not None]
    return values

def bfs(coordinates, r2= False ):
    end = [x for x,y in coordinates.items() if y == "E"][0]
    if r2:
        starts = [x for x,y in coordinates.items() if y == "a"]
    else:
        starts = [x for x,y in coordinates.items() if y == "S"]
    paths = []
    for start in starts:
        x,y = start
        queue = collections.deque([[(x,y)]])
        seen = set([(x,y)])

        while queue:
            path = queue.popleft()
            #print(f"sn {seen}")
            #print("path_len", len(path))
            x, y = path[-1]
            c = coordinates[x,y]
            if c == "S":
                c = "a"
            if c == "E":
                c = "z"
            xe,ye = end
            if (x ,y) == (xe,ye):
                paths.append(path)
                break
            for x in get_adjecent(x,y,coordinates):
                x2,y2,c2 = x
                if c2 == "E":
                    c2 = "z"
                if c2 == "S":
                    c2 = "a"
                diff_ord = (ord(c2) - ord(c)) < 2
                if (x2, y2) not in seen and diff_ord:
                    queue.append(path + [(x2, y2)])
                    seen.add((x2, y2))
    return paths


def translate(input_string):
    # Split the input string into a list of rows
    rows = input_string.strip().split("\n")

    # Create an empty list to hold the coordinates
    coordinates = {}
    height = 0
    # Loop through each row and each character in the row
    width = 0
    for y, row in enumerate(rows):
        height += 1
        width = 0
        for x, char in enumerate(row):
                width += 1

                coordinates[(x,y)] = char

    return width, height, coordinates

if __name__ == '__main__':
    with open("input.txt") as file:
        width, height, coordinates = translate(file.read())
    #get goal coordinate

    paths = bfs(coordinates)
    len_path_r1 = len(min(paths, key=len))
    print(f'R1: {len_path_r1-1}')

    paths = bfs(coordinates,True)
    len_path_r2 = len(min(paths, key=len))
    print(f'R2: {len_path_r2-1}')
