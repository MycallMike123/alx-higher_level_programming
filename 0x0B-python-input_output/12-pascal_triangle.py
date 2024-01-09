#!/usr/bin/python3
"""Defines a func Pascal's Triangle"""


def pascal_triangle(n):
    """Generates Pascal's triangle up to level n"""

    if n <= 0:
        return []

    tri = []
    for a in range(n):
        row = [1] * (a + 1)
        if a > 1:
            for b in range(1, a):
                row[b] = tri[a-1][b-1] + tri[a-1][b]
        tri.append(row)

    return tri
