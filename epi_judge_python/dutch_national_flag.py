import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)
from sys import exit


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    # TODO - you fill in here.
    
    # time complexity O(2n), space complexity o(1), where n is the length of A
    pivot = A[pivot_index]
    
    # print(pivot)
    
    smaller, greater_equal = 0, len(A)-1

    #first pass, such that A[:smaller] < pivot and A[greater_equal:] >= pivot    
    while smaller <= greater_equal:
        if A[smaller] >= pivot:
            A[greater_equal], A[smaller] = A[smaller], A[greater_equal]
            greater_equal -= 1
        else:
            smaller += 1
                        
        
    equal = smaller 
    greater = len(A) - 1 
    
    # second pass, such that A[smaller:equal] == pivot and A[equal:] > pivot
    while greater >= equal:
        if A[greater] == pivot:
            A[equal], A[greater] = A[greater], A[equal]
            equal += 1
        else:
            greater -= 1 
                
        
    # print(A)    
    return


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
