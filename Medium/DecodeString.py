# https://leetcode.com/problems/decode-string/
# incomplete and searched up answer

from typing import List
from string import ascii_lowercase


def decodeString(s: str) -> str:
    return decodeStringHelper(s, 0)


def decodeStringHelper(s: str, index: int):
    numbers = [str(x) for x in range(10)]

    tempString = ""

    while index != len(s):
        if s[index] in numbers:
            num, index = getK(s, index)
            index += 1

            tempString += num * decodeStringHelper(s, index)

            continue

        elif s[index] in ascii_lowercase:
            tempString += s[index]

        index += 1

    print(tempString)

    return tempString


def getK(s: str, index: int) -> List[int]:
    numbers = [str(x) for x in range(10)]

    walk = index

    while walk < len(s) and s[walk] in numbers:
        walk += 1

    num = int(s[index: walk])

    return [num, walk]


if __name__ == '__main__':
    decodeString("3[a]2[bc]")
    print()
    # decodeString("3[a2[c]]")

    # assert "aaabcbc" == decodeString("3[a]2[bc]")
    # assert "accaccacc" == decodeString("3[a2[c]]")
    # assert "abcabccdcdcdef" == decodeString("2[abc]3[cd]ef")
    # assert "abccdcdcdxyz" == decodeString("abc3[cd]xyz")

    pass
