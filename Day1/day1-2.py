import re
import sys
sys.path.append("..")
from input_reader import InputReader

def main():
    parens = InputReader.fetch_input()
    floor = 0
    for index, paren in enumerate(parens):
        floor += 1 if paren == "(" else -1
        if floor == -1:
            print(index + 1)
            break

main()
