def get_min(numbers):
    """ Return a new list with the smallest value in the input list.
    Before returning the new list, remove the value from the original list.

    >>> nums = [3, 4, 1]
    >>> get_min(nums)
    >>> [1]
    >>> nums
    >>> [3, 4]
    """

    # your code here
    ln = numbers[0]
    for n in range(len(numbers)):
        if numbers[n] < ln:
            ln = numbers[n]
    numbers.remove(ln)
    print(ln)
    print(numbers)

nums = [3, 4, 1]
get_min(nums)
    #>>> [1]
    #>>> [3, 4]