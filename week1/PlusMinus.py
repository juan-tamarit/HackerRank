#Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos=0
    neg=0
    null=0
    for n in arr:
        if n<0:
            neg+=1
        elif n>0:
            pos+=1
        else:
            null+=1
    resul_pos= pos/len(arr)
    resul_neg= neg/len(arr)
    resul_null= null/len(arr)
    
    print("%.6f" % resul_pos)
    print("%.6f" % resul_neg)
    print("%.6f" % resul_null)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
