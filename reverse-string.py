#!/usr/bin/python

# Implement a function that reverses a string 

str = input('Please input your string: ')

def reverse_str(str):
    '''
    Reverse the string.
    '''
    n = len(str) - 1
    rev_str = '' 
    for i in range(len(str)):
        rev_str += str[n] 
        n -= 1
    return rev_str


def another_rev(str):
    str = str[::-1]
    return str

print(reverse_str(str))

print(another_rev(str))
