# Replacing multiple characters in a string


def replace(text, old_chars, new_chars):
    """ Return text with old chars replaced with new chars.
    
    >>> replace('heWlXo theYreZ', 'WXYZ', 'YZWX')
    >>> 'heYlZo theWreX'
    """

    # your code here
    pos = []
    for i in range(len(old_chars)):
        pos.append(text.find(old_chars[i]))
    for i in range(len(old_chars)):
        text = text[:pos[i]] + new_chars[i] + text[pos[i]+1:]
    print(text)


replace('heWlXo theYreZ', 'WXYZ', 'YZWX')
    #>>> 'heYlZo theWreX'