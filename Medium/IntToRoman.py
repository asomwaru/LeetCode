# https://leetcode.com/problems/integer-to-roman/

def intToRoman(num: int) -> str:
    values = {
        "I":             1,
        "IV":            4,
        "V":             5,
        "IX":            9,
        "X":             10,
        "XL":            40,
        "L":             50,
        "XC":            90,
        "C":             100,
        "CD":            400,
        "D":             500,
        "CM":            900,
        "M":             1000,
    }

    roman = ""

    for symbol, number in list(values.items())[::-1]:
        if num == 0:
            return roman
        
        if len(symbol) == 2 and (num / number) == 1:
            roman += symbol
            num -= number
        else:
            repeats = num // number
            roman += symbol * repeats

            num -= repeats * number

    return roman    

if __name__ == '__main__':
    print(intToRoman(1994))
    pass