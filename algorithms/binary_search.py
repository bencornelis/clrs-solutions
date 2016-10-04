def binary_search(items, v):
    """
    Return index of v in items (sorted in increasing order) or None

    >>> binary_search([1,2,3,4,5,6], 5)
    4

    >>> binary_search([0,1,3,20,34,37,90], 20)
    3

    >>> binary_search([1,2,3,4,5,6], 8) is None
    True

    """
    return search(items, v, 0, len(items) - 1)

def search(items, v, r, s):
    """
    Input:
        items - sorted list
        v     - value
        r     - start index
        s     - stop index + 1

    """
    if r > s:
        return None
    else:
        m = r + (s - r)/2
        if v == items[m]:
            return m
        elif v > items[m]:
            return search(items, v, m + 1, s)
        else:
            return search(items, v, r, m - 1)

def iterative_binary_search(items, v):
    """
    Return index of v in items (sorted in increasing order) or None

    >>> iterative_binary_search([1,2,3,4,5,6], 5)
    4

    >>> iterative_binary_search([0,1,3,20,34,37,90], 20)
    3

    >>> iterative_binary_search([1,2,3,4,5,6], 8) is None
    True

    """
    r, s = 0, len(items) - 1
    while r <= s:
        m = r + (s - r)/2
        if v == items[m]:
            return m
        elif v > items[m]:
            r = m + 1
        else:
            s = m - 1
    return None

if __name__ == "__main__":
    import doctest
    doctest.testmod()
