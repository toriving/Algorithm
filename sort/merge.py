# merge sort
def merge_sort(list): #O(lg n)
    if len(list) <= 1:
        return list

    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]
    left = merge_sort(left)
    right = merge_sort(right)

    result = []

    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] > right[0]:
                result.append(right[0])
                right = right[1:]
            else:
                result.append(left[0])
                left = left[1:]

        elif len(left) > 0:
            result.extend(left)
            break

        elif len(right) > 0:
            result.extend(right)
            break

    list[:] = result
    return result