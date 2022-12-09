##I refused to hardmap coordinates since for r1 I could use prev coordinate 1 on 1 follow
#R2 introduced diag moving heads, which caused some issues with following h blindly at it's prev coordinate.
#now we had to also check if h moved diagonally and if so, either move t diag also, or if h would lie on the same column/row move 1 to h.

class coordinate():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x},{self.y}"

def adjacent(a, b):
    if a.x == b.x and abs(a.y - b.y) == 1:
        return True
    elif a.y == b.y and abs(a.x - b.x) == 1:
        return True
    #check if diagonal
    dx = abs(a.x - b.x)
    yx = abs(a.y - b.y)
    if (abs(a.x - b.x) == abs(a.y - b.y)) and (dx < 2 and yx <2):
        return True
    return False


def move(c: coordinate, dir:str):
    if dir == "U":
        res = coordinate(c.x, c.y+1)
    elif dir == "R":
        res = coordinate(c.x+1, c.y)
    elif dir == "L":
        res = coordinate(c.x-1, c.y)
    else:
        res = coordinate(c.x, c.y-1)
    return res

def check_how_to_move(t, h):
    dx = h.x - t.x
    dy = h.y - t.y
    if dx == 2 and dy == 0:
        return coordinate(t.x+1, t.y)
    if dy ==2 and dx == 0:
        return coordinate(t.x, t.y+1)
    if dy == -2 and dx == 0 :
        return coordinate(t.x, t.y-1)
    if dx == -2 and dy == 0:
        return coordinate(t.x-1, t.y)

def move_t(t: coordinate, h: coordinate, prev_h:coordinate):
    #print(f"h moved from {prev_h} to {h}, t is at {t}")
    if(adjacent(t,h)):
        return t
    ##check if h moved diagonally
    x_h_moved = h.x - prev_h.x
    y_h_moved = h.y - prev_h.y
    if abs(x_h_moved) == abs(y_h_moved):
        #wanted to avoid this hardmapping, but when a head moves twice diagonally it's impossible to use the prev coor to determine next coor
        #realised this is not entirely true, since when h moves double diag it must always lie one place further than adjacent on either the same
        #row or column as t when we want to not move diagonally as t.

        #check if h on collumn or row of t
        coor = check_how_to_move(t, h)
        if coor:
            #if so return a step in that dir
            return coor

        ##otherwise move diagonally same direction as h:
        return coordinate(t.x+x_h_moved, t.y+y_h_moved)
    return prev_h

def r1(lines):
    h_cor = coordinate(0, 0)
    t_cor = coordinate(0, 0)
    corrs_visited = [str(t_cor)]
    for line in lines:
        dir,num = line.split()
        for i in range(int(num)):
            prev_h_cor = h_cor
            h_cor = move(h_cor, dir)
            t_cor = move_t(t_cor, h_cor,prev_h_cor)
            corrs_visited.append(str(t_cor))
    corrs_visited = set(corrs_visited)
    print(f"r1: {len(corrs_visited)}")

def r2(lines):
    h_cor = coordinate(0, 0)
    t_cor = coordinate(0, 0)
    corrs_visited = [str(t_cor)]
    rope = {}
    rope_prev = {}
    for j in range(0,10):
        rope[j] = coordinate(0,0)
        rope_prev[j] = coordinate(0,0)
    for line in lines:
        dir,num = line.split()
        for i in range(int(num)):
            rope_prev[0] = h_cor
            h_cor = move(h_cor, dir)
            rope[0] = h_cor
            for j in range(1,10):
                rope_prev[j] = rope[j]
                t_cor = move_t(rope[j], rope[j-1],rope_prev[j-1])
                rope[j] = t_cor
            corrs_visited.append(str(rope[9]))

    corrs_visited = set(corrs_visited)
    print(f"r2: {len(corrs_visited)}")

if __name__ == '__main__':
    with open("input.txt") as file:
        lines = [line.rstrip('\n') for line in file]
    r1(lines)
    r2(lines)





