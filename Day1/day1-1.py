import re
import sys
sys.path.append("..")
from input_reader import InputReader

def main():
    parens = InputReader.fetch_input()
    floor = sum([ 1 if paren == "(" else -1 for paren in parens])
    print(floor)

main()
