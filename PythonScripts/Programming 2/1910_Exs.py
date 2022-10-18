# Write a function that gets an int number(n) as an input and prints all the ints smaller or equal to n that are perfect squares(x is a perfect square if it exists an int y so that x == y*y). The function returns the highest number printed.
# Write a function that gets an int number(n) as an input and prints all the ints smaller or equal to n that are powers of 2. The function returns the highest number printed.
# Write a function that gets two int numbers(a and b) as input and returns the sum of all odd numbers within the range(a and b included).
# Write a function that gets an int number(n) as an input and prints all its factors. The function returns the number of factors printed. For example, if n is 150, the function will print 2, 3, 5, 5.
# © Mattia Meligeni, October 18th 2022.

from math import sqrt, log


def isEven(n: int) -> bool:
    if (n % 2 == 0):
        return True
    else:
        return False


def myFirstFunc(n: int) -> int:
    max = 0
    for i in range(2, n+1):
        if sqrt(i).is_integer():
            print(i)
            if i > max:
                max = i
    return max


def mySecondFunc(n: int) -> int:
    max = 0
    for i in range(1, n+1):
        if log(i, 2).is_integer():
            print(i)
            if i > max:
                max = i
    return max


def myThirdFunc(a: int, b: int) -> int:
    sum = 0
    for i in range(a, b+1):
        if not (isEven(i)):
            sum += i

    return sum


def myFourthFunc(n: int):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    print(factors)
    return len(factors)


print("All the integers smaller or equal than 25 that are perfect squares: ")
myFirstFunc(25)
print()
print("All the integers smaller or equal than 64 that are powers of 2: ")
mySecondFunc(64)  # Technically 2^0 = 1, so 1 is a power of 2
print()
print("The sum of all the odds between 3 and 17 included: ", myThirdFunc(3, 17))
print()
print("All the factors of 240: ")
myFourthFunc(240)
