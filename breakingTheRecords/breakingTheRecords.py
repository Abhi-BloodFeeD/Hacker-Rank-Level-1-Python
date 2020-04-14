#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.


def breakingRecords(scores):
    highValue = scores[0]
    countHighScoreBreak = 0
    for score in scores:

        if score > highValue:
            highValue = score
            countHighScoreBreak += 1
        else:
            pass

    lowValue = scores[0]
    countLowScoreBreak = 0
    for scorez in scores:

        if scorez < lowValue:
            lowValue = scorez
            countLowScoreBreak += 1
        else:
            pass

    print(countHighScoreBreak, countLowScoreBreak)


if __name__ == '__main__':

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
