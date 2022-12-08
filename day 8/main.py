
from math import prod
nested_list_row = []
nested_list_row_dict =[]
x = []
visble_coor = []
test = ['0', '1', '1', '1']
dict = {}

def check_if_visible(idx, entry, set):
    can_see_left = True
    can_see_right = True
    idx_c = idx
    #stupid >= made me lose so much time
    while idx_c > 0:
        idx_c -= 1
        value = int(set[idx_c])
        if value >= entry:
            can_see_left = False
    idx_c = idx
    while idx_c < len(set)-1:
        idx_c += 1
        value = int(set[idx_c])
        if value >= entry:
            can_see_right = False

    return can_see_left or can_see_right


def check_view_blocked_total(idx, entry, set):
    idx_c = idx
    resa = 0
    resb = 0
    #print(f"{idx}, {entry}, {set}")
    while idx_c > 0:
        idx_c -= 1
        value = int(set[idx_c])
        if value >= entry:
            #print(idx - idx_c)
            if idx - idx_c < 2:
                resa = 1
                break
            else:
                resa = idx - idx_c
                break
        else:
            resa += 1

    idx_c = idx
    while idx_c < len(set)-1:
        idx_c += 1
        value = int(set[idx_c])
        if value >= entry:
            if idx_c - idx < 2:
                resb = 1
                break
            else:
                resb = idx_c - idx
                break
        else:
            resb += 1

    #print(f'left {resa} vs right {resb}')
    return resa*resb

def translate_coordinate_to_column(id, idx):
    column_id = idx
    column_idx = id
    return column_id, column_idx


def r1():
    visible = 0
    for id, set in enumerate(nested_list_row):
        for idx, entry in enumerate(set):
            entry = int(entry)
            #outer trees
            if idx == 0 or idx == len(set) - 1 or id == 0 or id == len(nested_list_row)-1:
                #print(f"In row {set}, index {idx + 1} with number {entry} is visible because it is on the edge")
                visible += 1
            else:
                if (check_if_visible(idx, entry, set)):
                    #print(f"In row {set}, index {idx+1} with number {entry} is visible")
                    visible += 1
                    c_id, c_idx = translate_coordinate_to_column(id,idx)
                    visble_coor.append((c_id,c_idx))

    for id, set in enumerate(nested_list_column):
        for idx, entry in enumerate(set):
            entry = int(entry)
            # outer trees get already added once
            if idx == 0 or idx == len(set)-1 or id == 0 or id == len(nested_list_column)-1:
                pass
            else:
                if (check_if_visible(idx, entry, set)):
                    has_been_seen = False
                    for x,y in visble_coor:
                        if x == id and y == idx:
                            #print(f"In column {set}, index {idx + 1} with number {entry} is not visible since it is already been seen before from another side")
                            has_been_seen = True
                    if not has_been_seen:
                        #print(f"In column {set}, index {idx+1} with number {entry} is visible")
                        visible += 1
    return visible


def r2():
    res = 0
    for id, set in enumerate(nested_list_row):
        for idx, entry in enumerate(set):
            entry = int(entry)
            total = check_view_blocked_total(idx, entry, set)
            c_id, c_idx = translate_coordinate_to_column(id, idx)
            dict[(c_id,c_idx)] = total

    for id, set in enumerate(nested_list_column):
        for idx, entry in enumerate(set):
            entry = int(entry)
            total = check_view_blocked_total(idx, entry, set)
            viewing_dist_row = dict[(id, idx)]
            total_sum = viewing_dist_row* total
            if total_sum > res:
                res = total_sum
    return res

if __name__ == '__main__':
    with open("input.txt") as file:
        lines = [line.rstrip('\n') for line in file]

    columns = zip(*lines)
    nested_list_column = [list(a) for a in columns]
    for line in lines:
        for char in line:
            x.append(char)
        nested_list_row.append(x)
        x = []

    #print(f'Column {nested_list_column}')
    #print(f'Row {nested_list_row}')
    visible = r1()
    sum = r2()

    print(f"Visible entries: {visible}")
    print(f"Best spot: {sum}")


