from hashlib import md5
import sys
sys.path.append("..")
from input_reader import InputReader

def main():
    secret_key = InputReader.fetch_input()
    done = False
    num = 0
    while not done:
        value_to_hash = secret_key + str(num)
        hex_value = md5(value_to_hash.encode()).hexdigest()
        first_6 = str(hex_value)[0:6]
        if first_6 == "000000":
            done = True
        else:
            num += 1
    print(num)

main()
