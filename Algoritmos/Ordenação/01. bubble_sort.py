def bubble_sort(array):
    length = len(array)-1
    for _ in range(length):
        has_trade = False
        for i in range(length):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                has_trade = True
        if not has_trade:
            break
    return array
