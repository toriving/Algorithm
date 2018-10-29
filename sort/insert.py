# insertion sort
def insert_sort(list): #O(n^2)
    for i in range(1, len(list)):
        j = i - 1
        key = list[i]
        while j >= 0 and list[j] > key:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key

    return list