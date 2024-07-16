def merge_sort(array):
    if len(array) <= 1:
        return array

    middle = len(array) // 2
    left_half = merge_sort(array[:middle])
    right_half = merge_sort(array[middle:])

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result
