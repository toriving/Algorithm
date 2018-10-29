from util import *

# quick sort
def rand_partition(list, start, end):
    i = random.randrange(start, end + 1)  # Can be inserted into the partition function.
    swap(list, start, i)
    return partition(list, start, end)

def partition(list, start, end): #O(n)
    x = list[start]
    i = start
    for j in range(start+1, end+1):
        if list[j] <= x:
            i += 1
            swap(list, i, j)
    swap(list, start, i)
    return i

def quick_sort(list, start, end): #O(lg n)
    if start < end:
        pivot = rand_partition(list, start, end)
        quick_sort(list, start, pivot - 1)
        quick_sort(list, pivot + 1, end)
    return list