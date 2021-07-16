# -*- coding: utf-8 -*-
"""
Created on Wednesday, 9th June 2021 7:56:52 pm
===============================================================================
@filename:  connect_four.py
@author:    Manuel Martinez (manmart@uchicago.edu)
@project:   mpcspe | 2018-19
@purpose:   connect-n
===============================================================================
"""
import sys
from typing import List


class Board:
    def __init__(self, x: int, y: int, n: int) -> None:
        if (2 > x > 100) | (2 > y > 100):
            raise ValueError('dimensions must be 2 <= dim <= 100')
        if (n > x) | (n > y):
            raise ValueError('violation: n > x || n > y')

        self.x = x
        self.y = y
        self.n = n
        self.data: List[List[int]] = [[0] * y for _ in range(x)]

    def add_cell(self, i: int, j: int, value: str) -> None:
        value = value.lower()
        if value == 'b':
            cell = -1
        elif value == 'r':
            cell = 1
        elif value == 'o':
            cell = 0
        else:
            raise ValueError(
                f'must only be `b`, `r` or `0`, currently {value}')

        self.data[i][j] = cell

    def check_neighbors(self, i: int, j: int) -> int:
        start = self.data[i][j]
        idxs = list(range(self.n))

        # check right
        try:
            right = all(start == self.data[i][j + k] for k in idxs)
            if right:
                return start
        except IndexError:
            pass

        # check down
        try:
            down = all(start == self.data[i - k][j] for k in idxs)
            if down:
                return start
        except IndexError:
            pass

        # check left diagonal
        try:
            diag = all(start == self.data[i - k][j - k] for k in idxs)
            if diag:
                return start
        except IndexError:
            pass

        # check right diagonal
        try:
            diag = all(start == self.data[i - k][j + k] for k in idxs)
            if diag:
                return start
        except IndexError:
            pass

        return 0

    def check_winner(self) -> str:
        playermap = {-1: 'blue', 1: 'red'}
        for i in reversed(range(self.x)):
            for j in range(self.y):
                check = self.check_neighbors(i, j)
                if check != 0:
                    return playermap[check]
        return 'none'


def main(line: str):
    for i, line in enumerate(line.splitlines()):
        if i == 0:
            x, y, n = map(int, line.split())
            board = Board(x=x, y=y, n=n)
        else:
            for j, cell in enumerate(line.split()):
                board.add_cell(i - 1, j, cell)

    winner = board.check_winner()
    if winner == 'none':
        sys.stdout.write(winner.upper())
    else:
        sys.stdout.write(f'{winner.upper()} WINS')


if __name__ == "__main__":
    main(sys.stdin.read())
