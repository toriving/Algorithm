from structure.heap import *

class priority_queue(heap):

    def __init__(self, array):
        super().__init__(array)
        self.build_heap()

    def insert(self, key): # O(lg n)
        self.heap_size = self.heap_size + 1
        self.A[self.heap_size] = -float('inf')
        self.increase_key(self.heap_size, key)

    def maximum(self):
        return self.A[1]

    def extract_max(self): # O(lg n)
        if self.heap_size < 1:
            print("heap underflow")
        max = self.A[1]
        self.A[1] = self.A[self.heap_size]
        self.heap_size = self.heap_size - 1
        self.heapify(1)

        return max

    def increase_key(self, i, key): # O(lg n)
        if key < self.A[i]:
            print("New key is smaller than current key.")
        self.A[i] = key
        while i > 1 and self.A[self.parent(i)] < self.A[i]:
            swap(self.A, i, self.parent(i))
            i = self.parent(i)


# A = [4,1,3,2,16,9,10,14,8,7]
# a = priority_queue(A)
# print(a.A)
# print(a.extract_max())
# print(a.maximum())
# a.increase_key(3,1111)
# a.insert(100)
# print(a.A)