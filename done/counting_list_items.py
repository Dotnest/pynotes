# Create a function that returns a dictionary of the items of a list
# and their counts.

def count_items(lst):    
    """ Return counts of the list items.
    
    >>> count_items(['one', 'two', 'two', 'three', 'three', 'three'])
    >>> {'one': 1, 'three': 3, 'two': 2}
    """

    # your code here

    items = lst
    counts = {}
    for item in items:
        if item not in counts:
            counts[item] = 1
        else:
            counts[item] += 1
    print(counts)

count_items(['one', 'two', 'two', 'three', 'three', 'three'])
#{'one': 1, 'three': 3, 'two': 2}

count_items(['one', 'two', 'two', 'three', 'three', 'three', 'two', 'three', 'three', 'three', 'four', 'dsfdsdfgfd', 1])
#{'one': 1, 'two': 3, 'three': 6, 'four': 1, 'dsfdsdfgfd': 1, 1: 1}