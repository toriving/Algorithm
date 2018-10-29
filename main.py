from sort import *
from search import *
import random

def sort_test(sort_function):
    small = random.sample(range(100),10)
    print('origin list :', small)
    print('sorted function :', sorted(small))
    # small = sort_function(small)
    small = sort_function(small, 99) # for counting sort
    # small = sort_function(small,0,9) # for quick sort
    print('your function :', small)

def search_test(search_function):
    small = random.sample(range(100), 10)
    small.sort()
    r = random.randrange(len(small))
    print(small, "\norigin -> index :", r, "value :", small[r])
    # index = search_function(small, small[r])  # for binary search
    # print("yours -> index :", index, "value :", small[index]) # for binary search
    index = search_function(small, 0, 9, r+1) # for smallest
    print("yours -> index :", r, "value :", index)

def main(task, function):
    task(function)

if __name__ == '__main__':
    # main(sort_test, counting_sort)
    main(search_test, rand_smallest)