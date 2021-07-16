# https://leetcode.com/problems/roman-to-integer/

def romanToInt(s: str) -> int:
    regular = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    odd = {
        "IX": 9,
        "IV": 4,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }

    total = 0
    odd_values = [x for x in list(odd.keys())[::-1] if x in s]

    for x in odd_values:
        s = s.replace(x, "")

    total += sum([odd[x] for x in odd_values])

    for x in s:
        total += regular[x]

    return total
