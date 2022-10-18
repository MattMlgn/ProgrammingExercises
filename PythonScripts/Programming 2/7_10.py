# we take 3 numbers x,y,z
# return the larger odd number or if
# no odd are given the minimum

from typing import List


def findMinimum(l: List[int]) -> int:

    return min(l)


def findMaximum(l: List[int]) -> int:

    return max(l)


def remove_odd(l: List[int]) -> List[int]:
    for i in l:
        if i % 2 != 0:
            l.remove(i)
    return l


def remove_even(l: List[int]) -> List[int]:
    for i in l:
        if i % 2 == 0:
            l.remove(i)
    return l


def computeNums(x: int, y: int, z: int) -> int:
    print(findMaximum(remove_even([x, y, z])))
    if (len(remove_even([x, y, z])) == 0):
        print(findMinimum([x, y, z]))


computeNums(10, 9, 3)
