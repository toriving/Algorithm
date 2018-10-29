def binary_search(list, n, left=0, right=9):  # Must use it in an array that is already sorted. O(lg n)
    if left > right:
        return False
    mid = (left + right) // 2
    if list[mid] > n:
        return binary_search(list, n, left, mid - 1)
    elif list[mid] < n:
        return binary_search(list, n, mid + 1, right)
    else:
        return mid

def binary_search2(list, n):
    left = 0
    right = len(list) - 1

    while left <= right:
        mid = (left + right) // 2
        temp = list[mid]
        if temp == n:
            return mid
        elif temp < n:
            left = mid + 1
        else:
            right = mid - 1

    return None