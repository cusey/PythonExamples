# python 3.5.2

import re


def Main():
    line = "I think I understand regular expressions"

    matchResult = re.match("think", line, re.IGNORECASE | re.MULTILINE)

    if matchResult:
        print("Match Found: " + matchResult.group())
    else:
        print("No match was found")


if __name__ == '__main__':
    Main()