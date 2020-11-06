#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 23:48:57 2020

@author: pepe
"""


# %%

def fib(n):

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)


fib(89)

# %%


def merge(left, right):
    result = []

    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)

    if len(left) == 0:
        result += right
    else:
        result += left

    return result


def mergesort(lst):

    if len(lst) <= 1:
        return lst

    middle = len(lst) // 2

    left = lst[0:middle]
    right = lst[middle:len(lst)]

    return merge(mergesort(left), mergesort(right))


mergesort([3, 2, 1, 2, 3, 4, 53, 88, 2, 12, 3, 4, 5, 2])
# %%
