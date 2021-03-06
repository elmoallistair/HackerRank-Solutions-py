# Written : 06-Jan-2020
# https://www.hackerrank.com/challenges/30-conditional-statements

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())  # Constraints: 1 <= n <= 100

    if n%2 == 1:    # If n is odd
        print('Weird')
    elif n%2 == 0:    # If n is even ...
        # ...and in the inclusive range of 2 to 5
        if n in range(2, 5+1):
            print('Not Weird')
        # ...and in the inclusive range of 6 to 20
        elif n in range(6, 20+1):
            print('Weird')
        # ...and greater than 20
        elif n > 20:
            print('Not Weird')

    # Shorter Code:
    # print('Weird' if n%2 == 1 or (n%2 == 0 and n in range(6, 20+1)) else 'Not Weird' if n%2 == 0 and (n in range(2, 5+1) or n > 20) else None)