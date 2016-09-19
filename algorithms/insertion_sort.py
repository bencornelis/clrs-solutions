def insertion_sort(items):
    """
    Return the items sorted using the insertion sort algorithm

    >>> insertion_sort([1,4,3,2,6])
    [1, 2, 3, 4, 6]

    >>> insertion_sort([9,1,-1,0,4,3])
    [-1, 0, 1, 3, 4, 9]

    >>> insertion_sort([3,1,0,1,-4,3])
    [-4, 0, 1, 1, 3, 3]
    
    """
    for j in range(1, len(items)):
        item = items[j]
        i = j - 1
        while i >= 0 and items[i] > item:
            items[i + 1] = items[i]
            i -= 1
        items[i + 1] = item
    return items

if __name__ == "__main__":
    import doctest
    doctest.testmod()
