# https://leetcode.com/problems/find-the-duplicate-number/

from typing import List


def findDuplicate(nums: List[int]) -> int:
    mapper = {}

    for n in range(len(nums)):
        current = nums[n]
        if current in mapper.keys():
            return current
        else:
            mapper[current] = 1

        print(mapper)


def main():
    print(findDuplicate([1, 3, 4, 2, 2]))


if __name__ == '__main__':
    main()
