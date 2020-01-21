import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

from sys import exit

# Returns the number of valid entries after deletion.
def delete_duplicates(A: List[int]) -> int:
    # TODO - you fill in here.
    l = len(A)
    for i in range(l):
        if i == 0:
            max_curent = A[i]
            A.append(A[i])
        elif A[i] > max_curent:
            max_curent = A[i]
            A.append(A[i])
            

    # A = A[l:] # 新的A的指针不同于原A
    for i in range(len(A) - l):
        A[i] = A[l+i]
            
            
            
    
    
    return len(A) - l


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    # print(len(A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_array_remove_dups.py',
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
