def recursive_binary_search(array, target, left=0, right=None):
    if right is None:
        right = len(array) - 1

    if left > right:
        return -1

    mid = (left + right) // 2

    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return recursive_binary_search(array, target, mid + 1, right)
    else:
        return recursive_binary_search(array, target, left, mid - 1)
