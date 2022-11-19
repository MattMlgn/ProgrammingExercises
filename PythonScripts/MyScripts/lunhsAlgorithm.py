def checkNumber(n: str) -> bool:
    str1 = ''.join(str(e) for e in [int(e)*2 for e in [e for i, e in enumerate(reversed(n)) if i%2 != 0]])
    return (sum(int(e) for e in str1) + sum(int(e) for i, e in enumerate(reversed(n)) if i % 2 == 0)) % 10 == 0

print(checkNumber("5227015713394942"))


