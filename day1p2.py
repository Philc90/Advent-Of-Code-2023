"""
--- Part Two ---

Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?

Your puzzle answer was 53312.
"""

import re
from fileReadUtil import fileToArray

example = [
    'two1nine',
    'eightwothree',
    'abcone2threexyz',
    'xtwone3four',
    '4nineeightseven2',
    'zoneight234',
    '7pqrstsixteen',
]

theInput = fileToArray('day1Input.txt')

wordsToNumStr = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'enin': '9',
    'thgie': '8',
    'neves': '7',
    'xis': '6',
    'evif': '5',
    'ruof': '4',
    'eerht': '3',
    'owt': '2',
    'eno': '1',
}

def firstAndLastDigit(theString):
    res = re.findall("(\d|one|two|three|four|five|six|seven|eight|nine)", theString)
    resRev = re.findall("(\d|enin|thgie|neves|xis|evif|ruof|eerht|owt|eno)", theString[::-1])

    # print(res[0], resRev[0])

    return convertToIntStr(res[0]) + convertToIntStr(resRev[0])

def convertToIntStr(theString):
    if theString.isdigit():
        return theString
    else:
        return wordsToNumStr[theString]

ans = 0
for elem in theInput:
    ans = ans + int(firstAndLastDigit(elem))
print(ans)
