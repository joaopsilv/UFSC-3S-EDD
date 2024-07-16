def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]
    left_half = []
    right_half = []

    for i in range(len(array)):
        if i == len(array) // 2:
            continue
        if array[i] < pivot:
            left_half.append(array[i])
        else:
            right_half.append(array[i])

    return quick_sort(left_half) + [pivot] + quick_sort(right_half)