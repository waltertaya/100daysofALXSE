#!/usr/bin/python3
'''
Tower of Hanoi implementation using python3
'''

def towerOfHanoi(n):
    '''
    Return number of moves and steps to solve
    '''
    number_of_moves = (2**n) - 1

    pegs = {
        'pegA': list(range(n, 0, -1)),
        'pegB': [],
        'pegC': []
    }

    # print(pegs['pegA'])
    # print(type(pegs))

    moves = []

    def move_disk(from_peg, to_peg):
        disk = pegs[from_peg].pop()
        pegs[to_peg].append(disk)
        moves.append(f"Move disk {disk} from {from_peg} to {to_peg}")

    def solve_hanoi(n, from_peg, to_peg, aux_peg):
        if n == 1:
            move_disk(from_peg, to_peg)
        else:
            solve_hanoi(n - 1, from_peg, aux_peg, to_peg)
            move_disk(from_peg, to_peg)
            solve_hanoi(n - 1, aux_peg, to_peg, from_peg)

    solve_hanoi(n, 'pegA', 'pegC', 'pegB')

    return number_of_moves, moves
