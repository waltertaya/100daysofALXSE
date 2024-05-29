#!/usr/bin/python3
'''
main.py
'''
import sys

if __name__ == '__main__':
    towerOfHanoi = __import__('tower-of_Hanoi').towerOfHanoi
    if (len(sys.argv) == 2):
        n = int(sys.argv[1])
    else:
        n = 3
    number_of_moves, moves = towerOfHanoi(n)
    print(f"Number of moves: {number_of_moves}")
    for move in moves:
        print(move)
