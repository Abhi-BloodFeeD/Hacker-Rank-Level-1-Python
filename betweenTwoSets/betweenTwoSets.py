# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
import math
import os
import random
import re
import sys
#


def getTotalX(a, b):

    value = 0
    for x in range(max(a), min(b) + 1):
        count = 0

        for elements in (a):
            if (x % elements == 0):

                count += 1
                pass
            else:
                break

        for elementz in (b):
            if (elementz % x == 0):

                count += 1
                pass
            else:
                break

        if count == (len(a) + len(b)):
            value += 1

    print(value)


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

arr = list(map(int, input().rstrip().split()))

brr = list(map(int, input().rstrip().split()))

total = getTotalX(arr, brr)
