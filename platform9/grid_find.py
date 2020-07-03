#!/usr/bin/env python3
"""
Platform9 interview questions:
Find the coordinates for all the matching words in the grid horizontally or vertically.
"""

import sys
import unittest

grid = [['A', 'F', 'H', 'D', 'T', 'K', 'P', 'E', 'P', 'G'],
        ['J', 'G', 'R', 'E', 'E', 'N', 'T', 'P', 'W', 'R'],
        ['U', 'R', 'G', 'E', 'P', 'Q', 'Y', 'K', 'W', 'E'],
        ['P', 'E', 'R', 'A', 'C', 'R', 'T', 'P', 'W', 'E'],
        ['U', 'E', 'F', 'J', 'T', 'U', 'W', 'P', 'Q', 'N'],
        ['P', 'N', 'U', 'S', 'N', 'W', 'A', 'Z', 'X', 'V']]

def find_word(target):
    """ Return the coordinates of the string horizontally or vertically in the grid.

    >>> find_word('GREEN')
    [(1, 1), (1, 1), (0, 9)]
    >>> find_word('ABSENT')
    []
    >>> find_word('PW')
    [(1, 7), (3, 7), (0, 8)]
    """
    results = []
    string = ""

    for a in range(0, len(grid)):
        for b in range(0, len(grid[a])):
            # Create strings on rows in the grid.
            string += grid[a][b]
        # Is the target is his string?
        if target in string:
            # Find the target by index in the string.
            index = string.index(target)
            # The target string was found at the row and index.
            results += [(a, index)]
        string = ""

    for b in range(0, len(grid[0])):
        for a in range(0, len(grid)):
            # Create strings based on the columns of the grid.
            string += grid[a][b]
        # Is the target in this string?
        if target in string:
            # Find the target by index in the string.
            index = string.index(target)
            # The target string was found at the index and column.
            results += [(index, b)]
        string = ""

    return results

def find_word2(target):
    """ Return the coordinates of the string horizontally or vertically in the grid.

    >>> find_word('GREEN')
    [(1, 1), (1, 1), (0, 9)]
    >>> find_word('ABSENT')
    []
    >>> find_word('PW')
    [(1, 7), (3, 7), (0, 8)]
    """
    results = []

    # Traverse the grid by row
    for column in range(0, len(grid)):
        # Create a string with the characters in the row.
        row = "".join(grid[column])
        # Is the target in the row?
        if target in row:
            # Find the target by index in the row.
            index = row.index(target)
            results += [(column, index)]
    # Transform the grid 90 degrees with the zip(*) method.
    row = 0
    for row2 in zip(*grid):
        # Create a string with the characters in the column.
        col2 = "".join(row2)
        # Is the target in the column?
        if target in col2:
            # Find the target by index in the column
            index = col2.index(target)
            results += [(index, row)]
        row += 1

    return results

class Tests(unittest.TestCase):
    """ Run a set of unit tests for these methods. """
    def test_find_word(self):
        """ Test the find_word() function. """
        self.assertEqual(find_word('GREEN'), [(1, 1), (1, 1), (0, 9)])
        self.assertEqual(find_word('ABSENT'), [])
        self.assertEqual(find_word('PW'), [(1, 7), (3, 7), (0, 8)])

    def test_find_word2(self):
        """ Test the find_word2() functions. """
        self.assertEqual(find_word2('GREEN'), [(1, 1), (1, 1), (0, 9)])
        self.assertEqual(find_word2('ABSENT'), [])
        self.assertEqual(find_word2('PW'), [(1, 7), (3, 7), (0, 8)])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(find_word(sys.argv[1]))
    else:
        print("Specify one argument a string to find in the grid.")
