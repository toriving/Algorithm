from structure.heap import *

def heap_sort(list): #O(nlg n)
    h = heap(list)
    h.heap_sort()
    return h.A[1:]
