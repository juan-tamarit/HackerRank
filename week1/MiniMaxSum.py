#Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    sum_array=sum(arr)
    min_array=sum_array
    max_array=0
    for n in arr:
        if sum_array-n<min_array:
            min_array=sum_array-n
        if sum_array-n>max_array:
            max_array=sum_array-n
    print(min_array,max_array," ")

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
