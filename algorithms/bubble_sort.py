def bubble_sort(items):
    """
    Return the items sorted using the bubble sort algorithm

    >>> bubble_sort([1,4,3,2,6])
    [1, 2, 3, 4, 6]

    >>> bubble_sort([9,1,-1,0,4,3])
    [-1, 0, 1, 3, 4, 9]

    >>> bubble_sort([3,1,0,1,-4,3])
    [-4, 0, 1, 1, 3, 3]

    """
    n = len(items)
    for i in range(n-1):
        for j in reversed(range(i+1, n)):
            if items[j] < items[j-1]:
                items[j-1], items[j] = items[j], items[j-1]
    return items

if __name__ == "__main__":
    import doctest
    doctest.testmod()
