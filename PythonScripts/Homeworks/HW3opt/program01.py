# -*- coding: utf-8 -*-

def findFrequency(s: str, t: str) -> int:
    fr = 0
    sub_len = len(t)
    for i in range(len(s)):
        if s[i:i+sub_len] == t:
            fr += 1
    return fr


def computeDics(file: str, min: int, max: int, n: int) -> list[dict]:
    dicList = [{}]
    string = computeFile(file)
    for i in range(min, max+1):
        dicList.append(mostFrequent(
            extractSubStrings(string, i)))
    dicList.pop(0)
    dicList.sort(key=lambda x: list(x))
    del dicList[n:]

    return dicList


def computeFile(file: str) -> str:
    file = open(file, 'r')

    lines = file.readlines()
    newLines = []

    for sub in lines:
        newLines.append(sub.replace("\n", ""))

    s = ""
    for t in newLines:
        s += t
    file.close()
    return s


def extractSubStrings(s: str, K: int) -> list[str]:
    res = [s[i: j] for i in range(len(s)) for j in range(
        i + 1, len(s) + 1) if len(s[i:j]) == K]
    return res


def mostFrequent(l: list[str]) -> str:
    res = {}
    res[l.count(max(set(l), key=l.count))] = max(set(l), key=l.count)
    return res


def ex1(text_file, min_len, max_len, n):
    return computeDics(text_file, min_len, max_len, n)


if __name__ == '__main__':
    # findFrequency(
    #    computeFile("ft1.txt"), "1000")
    #print(extractSubStrings(computeFile("ft1.txt"), 5))
    print(ex1("ft1.txt", 2, 4, 20))
