import string


def checkWord(s: string, g: string):
    if s == g:
        return "You Won!"
    for i in range(len(g)):
        return 0


print(checkWord("Night", input("Please input your guess: \n")))
