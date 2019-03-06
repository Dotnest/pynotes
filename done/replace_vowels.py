# Replacing vowels with whitespaces


def replace_vowels(text):
    """ Return the text after replacing the vowels in it with whitespaces.
    
    >>> replace_vowels("This Is fun.")
    >>> 'Th s  s f n.'
    """

    # your code here
    vowels = ('a', 'o', 'i', 'u', 'e')
    for vowel in vowels:
        while text.lower().find(vowel) != -1:
            posvowel = text.lower().find(vowel)
            text = text[:posvowel] + ' ' + text[posvowel+1:]
    print(text)


replace_vowels("This Is fun.")
    #>>> 'Th s  s f n.'