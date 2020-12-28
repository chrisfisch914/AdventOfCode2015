import re
import sys
sys.path.append("..")
from input_reader import InputReader

vowels = "aeiou"
banned_substrings = {"ab", "cd", "pq", "xy"}

def contains_pair_twice_without_overlap(word):
    for i in range(1, len(word)):
        curr_substring = word[i - 1] + word[i]
        for j in range(i + 2, len(word)):
            if curr_substring == (word[j - 1] + word[j]):
                return True
    return False

def char_repreated_with_seperator(word):
    for i in range(2, len(word)):
        if word[i - 2] == word[i]:
            return True
    return False

def is_nice_word(word):
    return contains_pair_twice_without_overlap(word) and char_repreated_with_seperator(word)

def main():
    nice_word_count = 0
    for word in InputReader.fetch_input_lines():
        if is_nice_word(word):
            nice_word_count += 1
    print(nice_word_count)

main()
