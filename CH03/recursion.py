"""
Lab 03: Recursion
Implement recursive functions from Chapter 3.

Every recursive function has two cases:
1. Base case - when the function doesn't call itself
2. Recursive case - when the function calls itself
"""
from typing import List


def countdown(i: int) -> None:
    # TODO: Implement countdown
    # 1. If i <= 0, print 0 and return
    # 2. Otherwise, print i
    # 3. Call countdown(i - 1)
     print(i)
     if i <=0:
         return 0
     else:
         return countdown(i-1)


def fact(x: int) -> int:
    # TODO: Implement factorial
    # 1. If x <= 1, return 1 (base case)
    # 2. Otherwise, return x * fact(x - 1)
     if x <= 1:
         return 1
     else:
         return x * fact(x-1)


def recursive_sum(arr: List[int]) -> int:
    # TODO: Implement recursive sum
    # 1. If array is empty, return 0 (base case)
    # 2. Otherwise, return arr[0] + recursive_sum(arr[1:])
    if len(arr) == 0:
        return 0
    return arr[0] +  recursive_sum(arr[1:])
         


def recursive_count(arr: List) -> int:
    # TODO: Implement recursive count
    # 1. If array is empty, return 0 (base case)
    # 2. Otherwise, return 1 + recursive_count(arr[1:])
    if len(arr) == 0:
        return 0
    return 1 +  recursive_count(arr[1:])

def recursive_max(arr: List[int]) -> int:
    """
    Find maximum element recursively.
    
    Base case: single element, return it
    Recursive case: max of (first, max of rest)
    """
    # TODO: Implement recursive max
    # 1. If len(arr) == 1, return arr[0] (base case)
    # 2. Get rest_max = recursive_max(arr[1:])
    # 3. Return arr[0] if arr[0] > rest_max else rest_max
    if len(arr) == 1:
        return arr[0]
    rest_max = recursive_max(arr[1:])
    return arr[0] if arr[0] > rest_max else rest_max
