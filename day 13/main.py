from ast import literal_eval
import functools
def convert_to_list(input):
    list_of_lists = []

    lines = input.strip().split("\n\n")


    for line in lines:
        pair = line.split("\n")
        x,y = pair

        literal_x = literal_eval(x)
        literal_y = literal_eval(y)

        list_of_lists.append((literal_x,literal_y))

    return list_of_lists


## could not use this r2 cause i started enumerating from the pairs.
## therefore i could not use this as a function in the sort key.
# i could rewrite this to evaluate_pair_r2 for r1 as well but time
def evaluate_pair(pairs):
    for idx, (e_x,e_y) in enumerate(pairs):
        #print(f"x: {e_x} vs y {e_y}")

        #first compare
        if isinstance(e_x, int) and isinstance(e_y, int):
            return e_x - e_y

        if isinstance(e_x, list) and isinstance(e_y, list):
            for x, y in zip(e_x, e_y):
                res = evaluate_pair([(x,y)])
                #if res is not 0 res and therefore order has been found
                if res != 0:
                    return res
            #if no order has been determined from every individual element because res is 0 for every element
            return len(e_x) - len(e_y)

        if isinstance(e_x, list) and isinstance(e_y, int):
            return evaluate_pair([tuple([e_x, [e_y]])])

        if isinstance(e_x, int) and isinstance(e_y, list):
            return evaluate_pair([tuple([[e_x], e_y])])

        return False

def evaluate_pair_r2(x,y):
        #print(f"x: {e_x} vs y {e_y}")

        #first compare
        if isinstance(x, int) and isinstance(y, int):
            return x - y

        if isinstance(x, list) and isinstance(y, list):
            for x_n, y_n in zip(x, y):
                res = evaluate_pair_r2(x_n,y_n)
                #if res is not 0 res and therefore order has been found
                if res != 0:
                    return res
            #if no order has been determined from every individual element because res is 0 for every element
            return len(x) - len(y)

        if isinstance(x, list) and isinstance(y, int):
            return evaluate_pair_r2(x,[y])

        if isinstance(x, int) and isinstance(y, list):
            return evaluate_pair_r2([x], y)

        return False

def r1(content):
    list_of_pairs = convert_to_list(content)
    list_of_index = []
    # for pair in list_of_pairs:
    for idx, pair in enumerate(list_of_pairs):
        res_i = evaluate_pair([pair])
        if res_i >= 0:
            # not in the right order
            continue
        else:
            # in the right order
            list_of_index.append(idx + 1)
        # print(f"res {res} for pair {pair}")
    print(f"F1 {sum(list_of_index)}")


def r2(content):
    content = [literal_eval(x) for x in content.splitlines() if x != '']
    content.append([[2]])
    content.append([[6]])
    list = sorted(content, key=functools.cmp_to_key(evaluate_pair_r2))

    first = list.index([[2]])+1
    second = list.index([[6]])+1
    print(f"F2 {first*second}")


if __name__ == '__main__':
    with open("input.txt") as file:
        content = file.read()
    r1(content)
    r2(content)



