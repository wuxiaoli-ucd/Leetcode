#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countResponseTimeRegressions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY responseTimes as parameter.
#

def countResponseTimeRegressions(responseTimes):
    # Write your code here
    if not responseTimes:
        return 0

    total = responseTimes[0]
    count = 0
    for i,v in enumerate(responseTimes[1:], start=1):
        average= total/i
        if v > average:
            count+=1
        total+=v
    return count


if __name__ == '__main__':
    responseTimes = [100, 200, 150, 300]
    result = countResponseTimeRegressions(responseTimes)
    print(result)