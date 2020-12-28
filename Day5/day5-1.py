import re
import sys
sys.path.append("..")
from input_reader import InputReader

def is_nice_word(word):
    num_vowels = 1 if word[0] in vowels else 0
    contains_dup = False
    for index in range(1, len(word)):
        substring = word[index - 1] + word[index]
        if substring in banned_substrings:
            return False
        if word[index - 1] == word[index]:
            contains_dup = True
        if word[index] in vowels:
            num_vowels += 1
    return num_vowels >= 3 and contains_dup

def main():
    nice_word_count = 0
    for word in InputReader.fetch_input_lines():
        if is_nice_word(word):
            nice_word_count += 1
    print(nice_word_count)

main()
