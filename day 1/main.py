# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open("input.txt") as file:
        lines = [line.rstrip('\n') for line in file]
    sum = 0
    sums = []
    biggest_sum = 0
    for line in lines:
        if line != '':
            num = int(line)
            sum += num
        else:
            sums.append(sum)
            if sum > biggest_sum:
                biggest_sum = sum
            sum = 0
    #last serie has no '' as end
    if sum > biggest_sum:
        biggest_sum = sum
    sums.append(sum)
    sums.sort()
    top_3 = sums[-3:]
    print(top_3)

    sum = 0



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
