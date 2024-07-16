def selection_sort(array):
    length = len(array)
    for i in range(length - 1):
        low_element_index = i
        for j in range(i + 1, length):
            if array[j] < array[low_element_index]:
                low_element_index = j
        if low_element_index != i:
            array[i], array[low_element_index] = array[low_element_index], array[i]
    return array
