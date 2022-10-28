# -*- coding: utf-8 -*-

""""
The standard encoding for Roman numerals follows the rules:
- there is no zero
- only the chars 'IVXLCDM' are used, which correspond to the decimal values
  'I' = 1, 'V' = 5, 'X' = 10, 'L' = 50, 'C' = 100, 'D' = 500, 'M' = 1000
- numbers are written from left to right, starting with higher values letters
  (thousands, hundreds, tens, units)
- the value of a Roman numeral is obtained by adding the values of the characters,
  EXCEPT when a character is followed by a higher-value character;
  in that case, the lower-value char is subtracted from instead of summed to
  the higher-value char
- at most, 3 equal symbols can be used together, only for the 'IXCM' ones
  ('III' = 3, 'XXX' = 30, 'CCC' = 300 , 'MMM' = 3000)
- to represent numbers containing digit 4 and/or 9, we use the subtraction from the
  symbol that follows
  e.g.: 4 = 'IV'   9 = 'IX',    40 = 'XL'    39 = 'IXL'   499 = 'ID'

The XKCD encoding

Let us now consider the Roman numerals encoding suggested by Randall Munroe in his XKCD blog.
He encodes each Roman symbol with the corresponding value and then joins all digits together.
E.g.    397 =>  'CCCXCVII' => 100 100 100 10 100 5 1 1 => '10010010010100511'
Let call this encoding "XKCD format".
To go back to our example, the XKCD sequence '10010010010100511' corresponds to 397.

The goal of this homework is to decode a list of strings representing Roman numerals
in the XKCD format, and return the K maximum corresponding values, in decreasing order.

Design and implement the following functions:

NOTICE: no other libraries are allowed.
"""


from audioop import reverse
from typing import final


def decode_XKCD_tuple(xkcd_values: tuple[str, ...], k: int) -> list[int]:
    '''
    Receives as arguments a list of strings representing values in the
    XKCD format, and a positive integer k <= len(xkcd_values).
    Decodes all XKCD formatted values and return the k higher values
    sorted in decreasing order.

    Parameters
    xkcd_values : list[str]     list of strings (values) in XKCD format
    k : int                     how many values to return
    Returns
    list[int]                   k maximum values in decreasing order
    '''
    xkcd_values_decoded = []
    finalValues = []
    for i in range(len(xkcd_values)):
        xkcd_values_decoded.append(decode_value(xkcd_values[i]))
    xkcd_values_decoded.sort(reverse=True)
    for i in range(k):
        finalValues.append(xkcd_values_decoded[i])

    return finalValues


def decode_value(xkcd: str) -> int:
    '''
    Decode a string representing a value in XKCD format
    and returns the corresponding decimal value (integer).

    Parameters
    xkcd : str                  string in XKCD format
    Returns
    int                         the corresponding value

    E.g.: '10010010010100511' -> 397
    '''
    return (list_of_weights_to_number(xkcd_to_list_of_weights(xkcd)))


def xkcd_to_list_of_weights(xkcd: str) -> list[int]:
    '''
    Splits an XKCD formatted string into the corresponding
    list of weights, each corresponding to one of the original roman
    numeral symbols the encoding is based on.

    Parameters
    xkcd : str              XKCD formatted string
    Returns
    list[int]               list of 'weights' corresponding to roman symbols

    E.g.: '10010010010100511' -> [100, 100, 100, 10, 100, 5, 1, 1,]
    '''
    admitted_List = ["1000", "500", "100", "50", "10", "5", "1"]
    finalList = []
    loop_out = 0
    while loop_out == 0:
        for roman_num in admitted_List:
            if (xkcd.startswith(roman_num)):
                finalList.append(int(roman_num))
                xkcd = xkcd[len(roman_num):]
                if len(xkcd) == 0:
                    loop_out = 1
                break
    return (finalList)


def list_of_weights_to_number(weigths: list[int]) -> int:
    '''
    Transforms a list of weights obtained from the XKCD format
    to the corresponding decimal value, by using the 'sum/subtract' rules.

    Parameters
    weights : list[int]    list of 'weights' of Roman numerals
    Returns
    int                    corresponding integer value

    E.g.: [100, 100, 100, 10, 100, 5, 1, 1,] -> 397
    '''
    arab = 0
    i = 0
    strange = False
    for index, n in enumerate(weigths):
        if index == len(weigths)-1:
            strange = True
            break
        if n < weigths[index+1]:
            continue
        else:
            break

    if strange:
        weigths.reverse()
        arab = weigths[0]
        for nu in weigths[1:]:
            arab -= nu
        return arab

    while i < len(weigths):
        if i == len(weigths)-1:
            arab += weigths[i]
            break
        if weigths[i] >= weigths[i+1]:
            arab += weigths[i]
        else:
            arab += weigths[i+1] - weigths[i]
            i += 1
        i += 1
    if arab >= 0:
        return arab
    else:
        return (arab * -1)


###################################################################################
if __name__ == '__main__':
    # add here your personal tests
    # print('10010010010100511', decode_value('10010010010100511'), '(397?)')
    #print(list_of_weights_to_number([10, 50, 1, 10]))
    # print(xkcd_to_list_of_weights("1050110"))
    print(decode_value("1101001000"))
    # print(decode_XKCD_tuple(
    #   ["150",  "1050110", "100100010100110", "11000", "1500", "10050010100110"], 6))
