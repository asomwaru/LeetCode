# https://leetcode.com/problems/rotate-image/
# didn't solve on own

from typing import List


def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    dimensions = len(matrix)

    for y in range(dimensions):
        for x in range(y, dimensions):
            temp = matrix[y][x]

            matrix[y][x] = matrix[x][y]
            matrix[x][y] = temp

    for y in range(dimensions):
        for x in range(dimensions // 2):
            temp = matrix[y][x]

            matrix[y][x] = matrix[y][dimensions-x-1]
            matrix[y][dimensions-x-1] = temp


def main():
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    rotate(mat)

    for x in mat:
        print(*x)


if __name__ == '__main__':
    main()
