# Sorted random floating numbers

from random import randint

def generate_floats(start, end, how_many):
    """ Return a list of sorted random floats in the (start, end) range.
    
    >>> generate_floats(3, 6, 5)
    >>> ['4.125', '4.622', '4.835', '4.981', '5.364']
    """

    # your code here
    floats = []
    for i in range(how_many):
        floats.append(randint(start*1000, end*1000) / 1000)
    floats.sort()
    print(floats)
    return floats

generate_floats(3, 6, 5)
#    >>> ['4.125', '4.622', '4.835', '4.981', '5.364']