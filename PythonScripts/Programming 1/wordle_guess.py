

def checkWord():
    tries = 1
    won = False
    s = "aceto"
    #  This is a side feature, not needed for the purpose of the exercise.
    incorrectChars = []
    while won != True and tries < 7:
        incorrectChars.sort()
        print("Incorrect characters are: ", incorrectChars)
        g = input("Please input your guess: \n")
        g = g.lower()
        if len(g) != 5:
            print("Error: guess must be 5 letters.")
            continue
        if g == s:
            print("You Won!")
            won = True
        else:
            for i in range(5):
                if g[i] in s:
                    if g[i] == s[i]:
                        print(g[i], "is green.")
                    else:
                        print(g[i], "is yellow.")
                else:
                    print(g[i], "is gray.")
                    if g[i] not in incorrectChars:
                        incorrectChars.append(g[i])

            tries += 1
    if not won:
        print("You lose and the word was:", s)


checkWord()
