# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import List


def letterCombinations(digits: str) -> List[str]:
    letterMap = {
        "2": ['a', 'b', 'c'],
        "3": ['d', 'e', 'f'],
        "4": ['g', 'h', 'i'],
        "5": ['j', 'k', 'l'],
        "6": ['m', 'n', 'o'],
        "7": ['p', 'q', 'r', 's'],
        "8": ['t', 'u', 'v'],
        "9": ['w', 'x', 'y', 'z'],
    }

    strings = []

    if digits == "":
        return strings

    permute("", letterMap, digits, strings)

    return strings


def permute(currentString: str, letterMap: dict, digits: str, strings: List[str]) -> str:
    if len(currentString) == len(digits):
        strings.append(currentString)
        return

    currentNum = digits[len(currentString)]

    for x in letterMap[currentNum]:
        currentString += x

        permute(currentString, letterMap, digits, strings)

        currentString = currentString[:-1]


def main():
    print(len(letterCombinations("234")))
    pass


if __name__ == '__main__':
    main()
