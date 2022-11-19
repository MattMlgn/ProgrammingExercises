# To order a list of strings considering the number of vowels in increasing order,
# then the whole length in increasing order, then the reverse alphabetical order.

l = ["plume", "pineapple", "pear", "peach", "blueberry", "apple", "aloe"]


def myorder(s):
    return -sum(c in "aeiou" for c in s), -len(s), s


print(sorted(l, key=myorder, reverse=True))

# To order a list of integers so that the odd numbers appear before the even numbers
# and the odd numbers are in increasing order, while the even numbers are in decreasing order.


def my2order(n):
    return -(n % 2), n if n % 2 else -n


ns = [3, 2, 5, 1, 6, 9, 7, 8]

#print(sorted(ns, key=my2order))
