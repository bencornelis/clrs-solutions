def selection_sort(items):
    """
    Return the items sorted using the selection sort algorithm

    >>> selection_sort([1,4,3,2,6])
    [1, 2, 3, 4, 6]

    >>> selection_sort([9,1,-1,0,4,3])
    [-1, 0, 1, 3, 4, 9]

    >>> selection_sort([3,1,0,1,-4,3])
    [-4, 0, 1, 1, 3, 3]

    """
    if is_sorted(items):
        return items

    n = len(items)
    for i in range(n-1):
        k = i
        for j in range(i+1, n):
            if items[j] < items[k]:
                k = j
        items[i], items[k] = items[k], items[i]
    return items

def is_sorted(items):
    for i in range(len(items)-1):
        if items[i] > items[i+1]:
            return False
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()
