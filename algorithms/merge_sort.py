def merge_sort(items):
    """
    Return the items sorted using the merge sort algorithm

    >>> merge_sort([1,4,3,2,6])
    [1, 2, 3, 4, 6]

    >>> merge_sort([9,1,-1,0,4,3])
    [-1, 0, 1, 3, 4, 9]

    >>> merge_sort([3,1,0,1,-4,3])
    [-4, 0, 1, 1, 3, 3]

    """
    n = len(items)
    if n == 1:
        return items
    else:
        l_items, r_items = items[0:n/2], items[n/2:n]
        return merge(merge_sort(l_items), merge_sort(r_items))

def merge(items1, items2):
    """
    Input: Two lists sorted in increasing order
    Return a sorted list that merges the two

    >>> merge([1,2,5,6], [2,4,7,8])
    [1, 2, 2, 4, 5, 6, 7, 8]

    """
    merged_items = []
    n1, n2 = len(items1), len(items2)

    # sentinel values
    items1.append(float("inf"))
    items2.append(float("inf"))

    i, j = 0, 0
    for k in range(n1 + n2):
        if items1[i] <= items2[j]:
            merged_items.append(items1[i])
            i += 1
        else:
            merged_items.append(items2[j])
            j += 1

    return merged_items


if __name__ == "__main__":
    import doctest
    doctest.testmod()
