def range_subset(x, y):
    if len(x) > 1 and x.step % y.step:
        return False  # must have a single value or integer multiple step
    return x.start in y and x[-1] in y

def r1(r1,r2):
    contains = range_subset(r1, r2)
    contains2 = range_subset(r2, r1)
    if contains or contains2:
        return 1
    return 0


def r2(r1, r2):
    list1 = []
    list2 = []
    list1.extend(r1)
    list2.extend(r2)
    a = set(list1)
    b = set(list2)
    if bool(set(a) & set(b)):
        return 1
    return 0


if __name__ == '__main__':
    with open("input.txt") as file:
        lines = [line.rstrip('\n').split(',') for line in file]
    pairs_r1 = 0
    pairs_r2 = 0
    for pair in lines:
        x,y = pair
        x1,x2 = x.split("-")
        y1,y2 = y.split("-")
        range1 = range(int(x1),int(x2)+1)
        range2 = range(int(y1),int(y2)+1)
        pairs_r1 += r1(range1,range2)
        pairs_r2 += r2(range1,range2)
    print(pairs_r1)
    print(pairs_r2)
