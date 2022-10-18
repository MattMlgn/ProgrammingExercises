# In our modern-day Gregorian calendar, three criteria must be taken into account to identify leap years:
# The year must be evenly divisible by 4;
# If the year can also be evenly divided by 100, it is not a leap year;
#     unless...
# The year is also evenly divisible by 400. Then it is a leap year.

# According to these rules, the years 2000 and 2400 are leap years,
# while 1800, 1900, 2100, 2200, 2300, and 2500 are not leap years.

# Write a Python function that, given a year, returns True if the year is a leap year, False otherwise.
# Test the program on the inputs: 2000 (True), 2400 (True), 1800 (False), 1900 (False), 2100 (False), 2200 (False), 2300 (False), 2500 (False).

def LeapYear(year):
    if year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 == 0:
        return False
    pass


if __name__ == "__main__":
    print(LeapYear(2000))
    print(LeapYear(1800))
