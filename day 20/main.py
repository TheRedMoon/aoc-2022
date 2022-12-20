



def parse_input(content):
    lines = content.splitlines()
    list_numbers = [int(x) for x in lines]
    res_numbers = []
    for idx, x in enumerate(list_numbers):
        res_numbers.append((idx,x))

    return res_numbers


def get_element_with_id(id, list):
    element = [tup for tup in list if tup[0] == id][0]
    index = [i for i, tup in enumerate(list) if tup[0] == id][0]
    return index, element

def get_element_with_move(move, list):
    element = [tup for tup in list if tup[1] == move][0]
    index = [i for i, tup in enumerate(list) if tup[1] == move][0]
    return index, element

def moves(move, list):
    id,move = move
    idx, element = get_element_with_id(id, list)
    new_idx = (idx + move) % (len(list)-1)

    list.insert(new_idx, list.pop(idx))
    return list


def go_round_in_cycles(res_list, number):
    idx,move = get_element_with_move(0,res_list)
    r1 = (number+idx) % len(res_list)
    return res_list[r1][1]

if __name__ == '__main__':
    with open("input.txt") as file:
        content = file.read()
    order_list = parse_input(content)
    res_list = order_list.copy()
    for move in order_list:
        res_list = moves(move,res_list)
    thousand = go_round_in_cycles(res_list,1000)
    thousand2 = go_round_in_cycles(res_list,2000)
    thousand3 = go_round_in_cycles(res_list,3000)

    print("r1 ", thousand+thousand2+thousand3)

    #r2
    decrypt_key = 811589153
    order_list = [(x,y*decrypt_key) for x,y in order_list]
    res_list = order_list.copy()
    for i in range(10):
        for move in order_list:
            res_list = moves(move,res_list)

    thousand = go_round_in_cycles(res_list,1000)
    thousand2 = go_round_in_cycles(res_list,2000)
    thousand3 = go_round_in_cycles(res_list,3000)

    print("r2 ", thousand+thousand2+thousand3)
