# https://leetcode.com/problems/find-all-duplicates-in-an-array/submissions/
from typing import List


def findAllDuplicates(nums: List[int]) -> List[int]:
    mapper = {}

    while len(nums) != 0:
        current = nums.pop()

        if current in mapper:
            mapper[current] += 1
        else:
            mapper[current] = 1

    return [x for x, y in mapper.items() if y > 1]


def main():
    print(findAllDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))


if __name__ == '__main__':
    main()
