# Written: 03-Apr-2020
# https://www.hackerrank.com/challenges/collections-counter/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

#!/usr/bin/env python3

import collections

def solution():
    X = int(input())
    lst = collections.Counter(map(int, input().split()))
    
    earned = 0
    N = int(input())
    for _ in range(N):
        size, price = map(int, input().split())
        if size in lst and lst[size]:
            lst[size] -= 1
            earned += price
    
    print(earned)

if __name__ == '__main__':
    solution()