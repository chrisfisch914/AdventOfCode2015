import re
import sys
sys.path.append("..")
from input_reader import InputReader

def parse_dimensions(dimensions):
    dimensions = dimensions.split("x")
    return int(dimensions[0]), int(dimensions[1]), int(dimensions[2])

def main():
    sq_feet_wrapping_paper = 0
    dimension_sets = InputReader.fetch_input_lines()
    for dimensions in dimension_sets:
        x, y, z = parse_dimensions(dimensions)
        xy = x * y
        xz = x * z
        yz = y * z
        sq_feet_wrapping_paper += (2 * xy) + (2 * xz) + (2 * yz) + min(xy, xz, yz)
    print(sq_feet_wrapping_paper)

main()
