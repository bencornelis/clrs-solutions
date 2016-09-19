# O(nlog(n)) using divide and conquer
def maximum_subarray(items, low, high):
    """
    Return tuple (low, high, sum) of the low and high index of the subarray,
    and its sum.

    >>> maximum_subarray([1,2,3,4,5,6], 0, 5)
    (0, 5, 21)

    >>> maximum_subarray([-7,-2,-3,-1,-8], 0, 4)
    (3, 3, -1)

    >>> maximum_subarray([13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7], 0, 15)
    (7, 10, 43)

    """
    if low == high:
        return (low, high, items[low])
    else:
        mid = (low + high)/2

        (left_low,  left_high,  left_sum)  = maximum_subarray(items, low, mid)
        (right_low, right_high, right_sum) = maximum_subarray(items, mid + 1, high)
        (cross_low, cross_high, cross_sum) = max_crossing_subarray(items, low, mid, high)

        max_sum = max(left_sum, right_sum, cross_sum)

        if left_sum == max_sum:
            return (left_low, left_high, left_sum)
        elif right_sum == max_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)

def max_crossing_subarray(items, low, mid, high):
    left_sum = -float("inf")
    total = 0
    for i in reversed(range(low, mid + 1)):
        total += items[i]
        if total > left_sum:
            left_sum = total
            max_left = i

    right_sum = -float("inf")
    total = 0
    for j in range(mid + 1, high + 1):
        total += items[j]
        if total > right_sum:
            right_sum = total
            max_right = j

    return (max_left, max_right, left_sum + right_sum)

# O(n) by keeping track of max subarray and right-anchored max subarray during linear pass
def max_subarray(items):
    """
    Return tuple (low, high, sum) of the low and high index of the subarray,
    and its sum.

    >>> max_subarray([1,2,3,4,5,6])
    (0, 5, 21)

    >>> max_subarray([-7,-2,-3,-1,-8])
    (3, 3, -1)

    >>> max_subarray([13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7])
    (7, 10, 43)

    """
    low, high, i = 0, 0, 0
    max_sum, max_right_sum = items[0], items[0]

    for j in range(len(items) - 1):
        if max_right_sum >= 0:
            max_right_sum += items[j+1]
        else:
            max_right_sum = items[j+1]
            i = j + 1

        if max_right_sum > max_sum:
            max_sum = max_right_sum
            low, high = i, j+1

    return (low, high, max_sum)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
