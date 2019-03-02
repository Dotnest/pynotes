# Find factorials of a list of numbers

def factorialize(numbers):
    """ Return factorials of a list of numbers.
    
    >>> factorialize([1, 2, 3, 4, 5])
    >>> [1, 2, 6, 24, 120]
    """

    # your code here
    for n in range(len(numbers)):
        f = 1
        while numbers[n] !=1:
            f *= numbers[n]
            numbers[n] -= 1
        numbers[n] = f
    print(numbers)


factorialize([1, 2, 3, 4, 5, 10])
#>>> [1, 2, 6, 24, 120, 3628800]