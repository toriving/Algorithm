from util import *

# counting sort
def counting_sort(A, k): # A is array, k is maximum number
    B = [0 for _ in A]
    C = [0 for _ in range(k+1)]

    for i in range(len(A)):
        C[A[i]] = C[A[i]] + 1
        # C[i] is count of i

    for j in range(k):
        C[j] = C[j] + C[j-1]
        # C[j] is count of element that is consisted of j and smaller than j

    for k in range(len(A)-1, -1, -1):
        B[C[A[k]]-1] = A[k]
        C[A[k]] = C[A[k]] - 1

    return B