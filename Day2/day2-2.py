import re
import sys
sys.path.append("..")
from input_reader import InputReader

def parse_dimensions(dimensions):
    dimensions = dimensions.split("x")
    return int(dimensions[0]), int(dimensions[1]), int(dimensions[2])

def main():
    ribbon_length = 0
    dimension_sets = InputReader.fetch_input_lines()
    for dimensions in dimension_sets:
        x, y, z = parse_dimensions(dimensions)
        xy = (2 * x) + (2 * y)
        xz = (2 * x) + (2 * z)
        yz = (2 * y) + (2 * z)
        ribbon_length += (x * y * z )+ min(xy, xz, yz)
    print(ribbon_length)

main()
