# https://youtu.be/khTiTSZ5QZY
# backtracking brute force solution

from typing import List
from functools import reduce


def prodArray(nums: List[int]) -> List[int]:
    newArr = []

    permute(nums, newArr, [], nums)

    return newArr


def permute(nums: List[int], newArray: List[int], currentArray: List[int], remainingNums: List[int]):
    if currentArray:
        prod = reduce(lambda x, y: x*y, currentArray)
    else:
        prod = None

    if prod and not prod in nums and prod not in newArray:
        newArray.append(prod)
        return

    for x in remainingNums:
        currentArray.append(x)

        permute(nums, newArray, currentArray, [
                n for n in remainingNums if n != x])

        currentArray.remove(x)


def main():
    arr = [1, 2, 3, 4]
    print(prodArray(arr))


if __name__ == '__main__':
    main()
