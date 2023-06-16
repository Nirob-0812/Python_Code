#!/bin/python3

import sys
def calculate_fib(n):
    sequence=[0,1]
    even_fib=[]
    while sequence[-1] <n:
        fib=sequence[-1]+sequence[-2]
        if(fib%2==0) and fib<n:
            even_fib.append(fib)
        sequence.append(fib)
    return sum(even_fib)


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    even_fib=calculate_fib(n)
    print(even_fib)

