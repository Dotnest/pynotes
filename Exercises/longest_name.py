def get_longest_name(a_list):
    """ Return '******' if the input list is [], [''], or a list containing
        names of equal length.
        Else, return the name that is greater in length than any other name
        in the list.
    
    >>> get_longest_name(["Candide", "Jessie", "Kath", "Amity", "Raeanne"])
    >>> '******'
    >>> get_longest_name(["Jessie", "Kath", "Amity", "Raeanne"])
    >>> 'Raeanne'
    >>> get_longest_name(["Jessie", "Kath", "Amity"])
    >>> 'Jessie'
    """

    # your code here
    ln = a_list[0]
    for name in a_list:
        if len(name) > len(ln):
            ln = name
        elif len(name) == len(ln) and a_list.index(name) != 0:
            ln = ''
            for _ in range(len(name)):
                ln += '*'
    print(ln)


get_longest_name(["Candide", "Jessie", "Kath", "Amity", "Raeanne"])
    #>>> '******'
get_longest_name(["Jessie", "Kath", "Amity", "Raeanne"])
    #>>> 'Raeanne'
get_longest_name(["Jessie", "Kath", "Amity"])
    #>>> 'Jessie'