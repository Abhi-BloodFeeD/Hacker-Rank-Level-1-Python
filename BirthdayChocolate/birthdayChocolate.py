#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.


def birthday(s, d, m):
    # sum should be equal to birthday--d
    # length --birth MOnth --m
    # array avaialable values = s
    #------WRITE CODE HERE------#


if __name__ == '__main__':

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)
