from collections import defaultdict
from pathlib import Path

dict = defaultdict(int)
path = Path("/")

if __name__ == '__main__':
    with open("input.txt") as file:
        lines = [line.rstrip('\n') for line in file]
    for line in lines:

        dirs = defaultdict(int)
        words = line.split()
        if {'$','cd'}.issubset(set(words)):
            dir = words[-1]
            path = path / dir
            path = path.resolve()
            print(f"path {path}")
        elif words[0].isnumeric():
            size = int(words[0])
            print(f'File {words[1]}, Size {words[0]}, for dir {path}')
            for new_path in [path,*path.parents]:
                dict[new_path] += size

            print("total size", dict[path])

    ##r2
    path = Path("/")
    path = path.resolve()
    un_used = 70000000 - dict[path]
    add_space = 30000000 - un_used
    print(f"Total space used: {dict[path]}. Space unused: {un_used}. Need {add_space} additional space. ")
    sum = 0
    for value in dict.values():
        if value <= 100000:
            sum+= value
    print(f'Final value r1 {sum}')

    dirs = []
    for value in dict.values():
        if value > add_space:
            dirs.append(value)
    dirs.sort()
    print(f'Final value r2 {dirs[0]}')

