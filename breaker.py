#!/bin/python3
#
# This program output in a file all possibilities for the text message
#

import sys

from string import (
    ascii_lowercase,
    ascii_uppercase,
)

small = list(ascii_lowercase)
big = list(ascii_uppercase)

i = 0
def break_this(message):
    "Breaking..."
    broken = []
    for dec in range(0,26):
        one_text = ''
        for letter in message:
            try:
                if letter in big:
                    pos = big.index(letter)
                    i =  (pos - dec) % 26
                    one_text += big[i]
                elif letter in small:
                    pos = small.index(letter)
                    i =  (pos - dec) % 26
                    one_text += small[i]   
                else:
                    one_text += letter 
            except ValueError:
                one_text += l
        broken.append(one_text)
    return broken

def save_in_file(filename, broken):
    print("Saving...")
    f = open(filename, "w")
    num = 0
    for i in broken:
        f.write('KEY = ' + str(num) + '\n')
        f.write(i)
        f.write('\n-----\n')
        num += 1

def print_help():
    print("./breaker <string_to_bruteforce> <filename_to_store_results>")

def main():
    if sys.argv[1] and sys.argv[2]:
        to_break = sys.argv[1]
        filename = sys.argv[2]
        broken = break_this(to_break)
        save_in_file(filename, broken)
        print("Results saved in : " + filename)
    else:
        print_help()


if __name__ == "__main__":
    main()
