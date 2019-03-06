# Use bubble sort to solve this problem.
# Wiki on the algorithm at https://en.wikipedia.org/wiki/Bubble_sort


def bubble_sort(numbers):
    """ Use bubble sort to sort a list of numbers in ascending order.
        Return the input list after mutating it with sorted numbers.
    >>> bubble_sort([2, 19, 4, 1, -40])
    [-40, 1, 2, 4, 19]
    >>> 
    """
    # your code here
    cleanpass = False
    while cleanpass == False:
        cleanpass = True
        for n in range(len(numbers)-1):
            if numbers[n] > numbers[n+1]:
                buffer = numbers[n]
                numbers[n] = numbers[n+1]
                numbers[n+1] = buffer
                cleanpass = False
    print(numbers)


bubble_sort([2, 19, 4, 1, -40])
#[-40, 1, 2, 4, 19]