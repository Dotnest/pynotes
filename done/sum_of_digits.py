# Recursively adding the digits of a number until the sum becomes a single digit

def sum_of_digits(number):
    """ Return sum of the digits of a number
    
    >>> sum_digits(1234)
    >>> 1
    """

    # your code here
    number = str(number)
    while len(number) != 1:
        sum = 0
        for i in range(len(number)):
            sum += int(number[i])
        number = str(sum)
    print(number)

sum_of_digits(1234)
#    >>> 1
sum_of_digits(88)
sum_of_digits(1)
sum_of_digits(90)