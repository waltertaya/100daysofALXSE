#!/usr/bin/env python3
''' Positional Arguments
Unpacking list to form positional arguments
'''


def function(a, b, c, *args):
    print(f'a: {a}, b: {b}, c: {c}')
    print(f'args: {args}')

if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5]
    function(*my_list)

    function(1, 2, 3, 4, 5)
    function(1, 2, 3)
