# Find the i-th smallest element.

from sort.quick import *

def rand_smallest(A, p, r, i=0):
    if p == r:
        return A[p]
    q = rand_partition(A, p, r)
    k = q - p + 1
    if i == k:
        return A[q]
    elif i < k:
        return rand_smallest(A, p, q - 1, i)
    else:
        return rand_smallest(A, q + 1, r, i - k)

