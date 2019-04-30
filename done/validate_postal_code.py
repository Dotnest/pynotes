# Validate Postal Code (Canadian)

"""

Define a function postalValidate(S) which first checks if S represents
a postal code (Canadian) which is valid:

    first, delete all spaces;
    the remainder must be of the form L#L#L# where L are letters
    (in either lower or upper case) and # are numbers.
    
If S is not a valid postal code, return the boolean False.
If S is valid, return a version of the same postal code in the nice format
L#L#L# where each L is capital.

Use the following methods to do this exercise:
str.replace(), str.isalpha(), str.isdigit(), and str.upper()

"""

def postalValidate(S):
    """ Return False if S is not a valid postal code.
    If S is valid, return it in the format L#L#L# where each L is capital.
    
    >>> postalValidate(' d3 L3 T3')
    >>> 'D3L3T3'
    """

    # your code here
    S = S.upper().replace(" ", "")
    if len(S) == 6:
        if S[0].isalpha() and S[2].isalpha() and S[4].isalpha() and S[1].isdigit() and S[3].isdigit() and S[5].isdigit():
            print(S)
        else:
            print('False:', S)
    else:
        print('False:', S)


# Use these arguments to test your function.

postalValidate('postal')
postalValidate('H0H0H0')
postalValidate(' d3 L3 T3')
postalValidate(' 3d3 L3 T')
postalValidate('n21 3g1z')
postalValidate('V4L1D')
postalValidate('K1A 0A3')
postalValidate('H0H0H')
