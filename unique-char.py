#!/usr/bin/python

#determine if a string has all unique characters.

phrase = input("Please input the phrase: ")
print(phrase)

def unique(phrase):
    '''
    Determines if the string has all unique characters.
    '''
    phrase = sorted(phrase)
    for i in range(len(phrase)-1):
        if phrase[i] == phrase[i+1]:
            return False
    return True

print(unique(phrase))
