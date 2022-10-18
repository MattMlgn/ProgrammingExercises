from math import sqrt


def computeX(a: int, b: int, c: int) -> str:
    d = b**2 - 4 * a * c
    if d < 0:
        raise ("Discriminant error", "Not defined in real numbers.")
    if a == 0:
        return -b/c
    x1 = (-b - sqrt(d)) / (2 * a)
    x2 = (-b + sqrt(d)) / (2 * a)
    if x1 == x2:
        return x1
    return f'Solutions are: {x1} and {x2} and the max is {max(x1,x2)}'


print(computeX(int(input("Please input the a parameter: \n")), int(input(
    "Please input the b parameter: \n")), int(input("Please input the c parameter: \n"))))
