import re
import sys
sys.path.append("..")
from input_reader import InputReader

def coord_to_key(x, y):
    return str(x) + "," + str(y)

def main():
    x = 0
    y = 0
    presents = 1
    visited = {coord_to_key(0,0)}
    directions = InputReader.fetch_input()
    for direction in directions:
        if direction == "^":
            y += 1
        elif direction == "v":
            y -= 1
        elif direction == ">":
            x += 1
        else:
            x -= 1
        if not coord_to_key(x, y) in visited:
            presents += 1
            visited.add(coord_to_key(x, y))
    print(presents)

main()