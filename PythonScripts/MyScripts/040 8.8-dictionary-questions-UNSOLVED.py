# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 17:32:12 2019

@author: giles
"""

from time import perf_counter

'''
Question 1
Can you remember how to check if a key exists in a dictionary?
Using the capitals dictionary below write some code to ask the user to input
a country, then check to see if that country is in the dictionary and if it is
print the capital. If not tell the user it's not there.
'''

capitals = {'France':'Paris','Spain':'Madrid','United Kingdom':'London',
            'India':'New Delhi','United States':'Washington DC','Italy':'Rome',
            'Denmark':'Copenhagen','Germany':'Berlin','Greece':'Athens',
            'Bulgaria':'Sofia','Ireland':'Dublin','Mexico':'Mexico City'
            }
# check = input("Input a country to search the capital of: ")
# if check in capitals: print(capitals[check]) 
# else: print("not here")

'''
Question 2
Write python code that will create a dictionary containing key, value pairs
that represent the first 12 values of the Fibonacci sequence
i.e {1:0,2:1,3:1,4:2,5:3,6:5,7:8 etc}
'''
# fibonacci= {}
# my_list =[]
# first= 0
# second = 1
# third = 0

# for i in range(100000):
#     third = first + second
#     fibonacci[i] = third
#     my_list.append(third)
#     first = second
#     second = third

# start_time = perf_counter()

# print(fibonacci[67898])

# end_time = start_time = perf_counter()
# print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')

# start_time = perf_counter()

# print(my_list[67898])

# end_time = start_time = perf_counter()
# print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')




'''
Question 3
Create a dictionary to represent the open, high, low, close share price data
for 4 imaginary companies. 'Python DS', 'PythonSoft', 'Pythazon' and 'Pybook'
the 4 sets of data are [12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
[98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]
'''
companies = {
    "Python DS" : {"open": 12.87,"high": 13.23, "low": 11.42, "close": 13.10},
}
print(companies['Python DS']["open"])



'''
Question 4
Go to the python module web page and find a module that you like. Play with it,
read the documentation and try to implement it.
'''


'''
Question 5
Create a dictoinary containing as keys the letters from A-Z, the values should
be random numbers created from the random module. Can you draw a bar graph of
the results?
'''


'''
Question 6
Create a dictionary containing 4 suits of 13 cards
['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
'''
