
# link : https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one

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
    # Write your code here
    pos_num = [i for i in arr if i > 0]
    neg_num = [i for i in arr if i < 0]
    zero_num = [i for i in arr if i == 0]
    pos = len(pos_num)/len(arr)
    neg = len(neg_num)/len(arr)
    zero = len(zero_num)/len(arr)
    print(f'{pos:.5f}')
    print(f'{neg:.5f}')
    print(f'{zero:.5f}')
      

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)