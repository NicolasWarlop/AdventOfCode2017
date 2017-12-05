""" 2017d4.py - Advent of code 2017 - day 4"""
import re

def contains_no_duplicates(line):
    """ Does the string contain duplicate words?"""
    passphrase = re.split(r'\W+', line)
    for word in passphrase:
        if passphrase.count(word) > 1:
            return False
    return True

def contains_no_anagrams(line):
    """ Does the string contain anagram words?"""
    passphrase = re.split(r'\W+', line)

    #Sort the strings alphabetically
    passphrase = [''.join(sorted(i)) for i in passphrase]
    for word in passphrase:
        if passphrase.count(word) > 1:
            return False
    return True

def main():
    """main function"""
    valid_phrases = 0
    valid_phrases_2 = 0
    inputfile = open('d4input.txt', 'r')

    #split the line based off of the tab delimitor
    for line in inputfile:
        if contains_no_duplicates(line):
            valid_phrases += 1
        if contains_no_anagrams(line):
            valid_phrases_2 += 1

    print("part 1: " + str(valid_phrases))
    print("part 2: " + str(valid_phrases_2))

#Main execution
if __name__ == "__main__":
    main()
