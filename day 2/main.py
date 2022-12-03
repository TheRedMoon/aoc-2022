# A rock
# B paper
# c siccor
# x rock
# y paper
# z scissors

def win(elf):
    if elf == "A":
        return "B"
    elif elf == "B":
        return "C"
    else:
        return "A"

def lose(elf):
    if elf == "A":
        return "C"
    elif elf == "B":
        return "A"
    else:
        return "B"

def draw(elf):
    return elf


def determine_choice(elf, you ):
    if you == "X":
        choice = lose(elf)
    elif you == "Y":
        choice = draw(elf)
    else:
        choice = win(elf)

    return choice



def translate_choice_to_points(choice):
    if choice == "A":
        return 1
    if choice == "B":
        return 2
    if choice == "C":
        return 3

def determine_result_you(elf, you):
    if elf == you:
        return 3
    if ((elf == "A" and you == "C") or (elf == "B" and you == "A") or (elf == "C" and you == "B")):
        return 0
    else:
        return 6



def simulate_round(elf, you ):
    points = 0
    points += determine_result_you(elf, you)
    points += translate_choice_to_points(you)
    return points


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open("input.txt") as file:
        lines = [line.rstrip('\n') for line in file]
    total_points = 0
    for line in lines:
        elf,you = line.split()
        choice = determine_choice(elf,you)
        total_points += simulate_round(elf,choice)

    print(f"total_points: {total_points}")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
