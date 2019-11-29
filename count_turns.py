#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countLuck function below.
def count_luck(matrix, k):
    total_rows = len(matrix[0])
    total_cols = len(matrix)

    def walk_next_col(cell):
        return cell + 1 if total_cols >= (cell + 1) else 'None'

    def walk_prev_col(cell):
        return cell - 1 if 0 <= (cell - 1) else 'None'

    def walk_next_row(cell):
        return cell + 1 if total_rows >= (cell + 1) else 'None'

    def walk_prev_row(cell):
        return cell - 1 if 0 <= (cell - 1) else 'None'

    #  look for M


    m_row = None
    m_col = None

    path = []
    for row in matrix:
        if 'M' in matrix[row]:
            m_row = row
            m_col = matrix[row].index('M')
            break


    i = 0
    while True:
        path[i] = {
            'location': [m_row, m_col],
            'row': m_row,
            'col': m_col,
            'prev': None,
            'next': None,
            'turn': False,
            'possible_moves': {
                'l': [m_row, walk_prev_col(m_col)],
                'r': [m_row, walk_next_col(m_col)],
                'u': [walk_prev_row(m_row), m_col],
                'd': [walk_next_row(m_row), m_col]
            }
        }

        for pm_k, pm_v in path[i].get('possible_moves'):
            print(pm_v)
        break

    print(path)

if __name__ == '__main__':
    matrix = {}
    matrix[0] = ['.', 'X', '.', 'X', '.', '.', '.', '.', '.', '.', 'X']
    matrix[1] = ['.', 'X', '*', '.', 'X', '.', 'X', 'X', 'X', '.', 'X']
    matrix[2] = ['.', 'X', 'X', '.', 'X', '.', 'X', 'M', '.', '.', '.']
    matrix[3] = ['.', '.', '.', '.', '.', '.', 'X', 'X', 'X', 'X', '.']
    k = 1
    print(k)
    print(count_luck(matrix, k))
