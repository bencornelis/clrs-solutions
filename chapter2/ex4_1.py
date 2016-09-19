def add_binary_integers(a_bits, b_bits):
    """
    Return sum in binary form as an (n+1)-element array

    >>> add_binary_integers([1, 0, 1], [1, 1, 1])
    [1, 1, 0, 0]

    """
    sum_bits = []
    carry = 0
    for a, b in reversed(zip(a_bits, b_bits)):
        carry, sum_bit = divmod(a + b + carry, 2)
        sum_bits.insert(0, sum_bit)
    sum_bits.insert(0, carry)

    return sum_bits

if __name__ == "__main__":
    import doctest
    doctest.testmod()
