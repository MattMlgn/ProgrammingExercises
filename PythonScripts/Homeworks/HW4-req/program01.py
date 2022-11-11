#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# This function take a string in input and returns a tuple, with the filename of the next file, and all the words in the file.
def computeFile(filename: str):
    with open(filename, "r") as file:
        return file.readline().strip(), file.read().split()


# This function takes in input a string that represent the initial file.
def computeFolder(start: str) -> list[str]:
    nextFile, initialWords = computeFile(start)
    while nextFile != start:
        initialWords.extend(computeFile(nextFile)[1])
        nextFile = computeFile(nextFile)[0]
    return initialWords


def mostFrequent(lst: list[str]) -> str:
    dic = {}
    count, itm = 0, ''
    for item in reversed(sorted(lst)):
        dic[item] = dic.get(item, 0) + 1
        if dic[item] >= count:
            count, itm = dic[item], item
    return (itm)


def most_frequent_chars(filename: str) -> str:
    # sourcery skip: use-contextlib-suppress
    words = computeFolder(filename)
    maxOccurs = ""
    listOfChars = []
    for i in range(len(max(words, key=len))):
        for item in words:
            try:
                listOfChars.append(item[i])
            except IndexError:
                pass

        maxOccurs += mostFrequent(listOfChars)
        listOfChars.clear()
    return maxOccurs
