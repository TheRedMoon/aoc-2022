import re

def parse_content(line):
    res = re.findall(r"-?\d+", line)
    res = [int(x) for x in res]
    return res

def calculate_manhattan(sx, sy, bx, by):
    # |x1 - x2| + |y1 - y2|
    return abs(sx-bx) + abs(sy-by)

def r1(sensors, beacons):
    y_c = 2000000 #y is 200000, did not see this in the assignment at first... :(
    found = 0
    for x in range(-4878878, 4878878):
        for sensor in sensors:
            sx,sy,man = sensor
            # check coordinate that have a smaller manhattan dist than the man found:
            # man_coordi <= man_beacon
            smaller = man >= (abs(x-sx)+abs(y_c-sy))
            #check if closer and also skip the beacon itself
            if smaller and (x,y_c) not in beacons:
                found += 1
                #dont count multiple times, once per sensor is enough
                break

    print(f"R1 found {found}")

def check_if_bigger_than_all_manhatans(x,y,sensors):
    if not (0 <= x <= 4000000 and 0 <= y <= 4000000):
        return False
    for sensor in sensors:
        sx,sy,man = sensor

        smaller = man >= (abs(x-sx)+abs(y-sy))
        if smaller:
            return False
    return True


def r2(sensors, beacons):
    #the only possible beacon location that has not be found must be larger than any man dist found yet
    #we need to find this coordinate that lies exactly one further than every man dist

    #loop over man dist:
    for sensor in sensors:
        x,y,manhattan_dist = sensor
        new_dist = manhattan_dist+1


        for i in range(0, new_dist+1):
            dy = new_dist-i

            #east
            x1 = x+dy
            y1 = y+i
            if(check_if_bigger_than_all_manhatans(x1,y1, sensors)):
                return x1 * 4000000 + y1

            #west
            x1 = x-dy
            y1 = y+i
            if (check_if_bigger_than_all_manhatans(x1, y1, sensors)):
                return x1 * 4000000 + y1

            #north
            x1 = x+i
            y1 = y+dy
            if (check_if_bigger_than_all_manhatans(x1, y1, sensors)):
                return x1 * 4000000 + y1

            #south
            x1 = x+i
            y1 = y-dy
            if (check_if_bigger_than_all_manhatans(x1, y1, sensors)):
                return x1 * 4000000 + y1

if __name__ == '__main__':
    with open("input.txt") as file:
        content = file.read()
    sensors = []
    beacons = set()
    for line in content.splitlines():
        coordinates = parse_content(line)
        sx,sy,bx,by = coordinates
        #manhattan distance
        manhattan_dist = calculate_manhattan(sx,sy,bx,by)
        sensors.append((sx,sy, manhattan_dist))
        beacons.add((bx,by))

    r1(sensors, beacons)

    print(r2(sensors,beacons))





