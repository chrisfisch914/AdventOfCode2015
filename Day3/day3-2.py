import re
import sys
sys.path.append("..")
from input_reader import InputReader

def coord_to_key(x, y):
    return str(x) + "," + str(y)

def update_coord(x, y, direction, visited):
    if direction == "^":
            y += 1
    elif direction == "v":
        y -= 1
    elif direction == ">":
        x += 1
    else:
        x -= 1
    if not coord_to_key(x, y) in visited:
        visited.add(coord_to_key(x, y))
    return x, y

def main():
    santa_x = 0
    santa_y = 0
    robo_x = 0
    robo_y = 0
    visited = {coord_to_key(0,0)}
    directions = InputReader.fetch_input()
    for index, direction in enumerate(directions):
        if index % 2 == 0:
            santa_x, santa_y = update_coord(santa_x, santa_y, direction, visited)
        else:
            robo_x, robo_y = update_coord(robo_x, robo_y, direction, visited)
    print(len(visited))

main()