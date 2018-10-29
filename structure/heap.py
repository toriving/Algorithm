from util import *

class heap:
    # A : array, i : index, k : key
    def __init__(self, array):
        self.A = [None] + array
        self.length = len(self.A)  - 1 # length of array
        self.heap_size = self.length

    def parent(self, i):
        return i//2

    def left(self, i):
        return 2 * i

    def right(self, i):
        return 2 * i + 1

    def heapify(self, i):  # O(lg n)
        l = self.left(i)
        r = self.right(i)

        if l <= self.heap_size and self.A[l] > self.A[i]:
            largest = l
        else:
            largest = i

        if r <= self.heap_size and self.A[r] > self.A[largest]:
            largest = r

        if largest != i:
            swap(self.A, i, largest)
            self.heapify(largest)

    def build_heap(self): #O(n)
        for i in range(self.length//2, 0, -1):
            self.heapify(i)

    def heap_sort(self): #O(nlg n)
        self.build_heap()
        for i in range(self.length, 1, -1):
            swap(self.A, 1, i)
            self.heap_size = self.heap_size - 1
            self.heapify(1)



