# Four fours challenge
#Filename: fourfours.py
# ©2022 Mattia Meligeni
#
#

def printResult(n: int) -> str:
    result = {0: "4 + 4 - 4 - 4",
              1: "(4+4)/(4+4)", 2: "(4+4-4-√4)", 3: "(4+4+4)/4", 4: "4! - (4*4) - 4", 5: "(4 * 4 + 4)/4", 6: "(4! + 4 - 4) / 4", 7: " 4 + 4 - 4 ÷ 4",
              8: "4 ÷ 4 * 4 + 4", 9: "4 ÷ 4 + 4 + 4", 11: "(4!*√4 - 4)÷ 4", 12: "4 *(4 - 4 ÷ 4)", 13: "(4!*√4 + 4)÷ 4", 14: "4 * 4 - 4 ÷√4",
              15: "4 * 4 - 4 ÷ 4", 16: "4 * 4 + 4 - 4", 17: "4 * 4 + 4 ÷ 4", 18: "4 * 4 + 4 -√4", 19: "4!-(4 + 4 ÷ 4)", 20: "4 *(4 ÷ 4 + 4)"}
    if n == 99:
        exit(0)
    elif n > 20:
        print("Error number must be between 0 and 20.")
        exit(1)

    return result[n]


s = int(input("Hello and welcome to the four fours challenge! Please insert a number up to 20 or 99 to exit:\n"))
print("You can make:", s, "by doing:", printResult(s))
