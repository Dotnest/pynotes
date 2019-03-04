# Pick words of certain length from a string, but ignore punctuation


def find_words_of_length(number, text):
    """ Remove punctuation from text, then return words of length number.
    
    >>> find_words_of_length(4, "this is a string with some four-letter words.")
    >>> ['this', 'with', 'some']
    """

    # your code here
    textlist = text.split(' ')
    punctuation = ('!', '?', '?!', ',', '.', ':', ';', '(', ' )', '-')
    for word in textlist:
        if word.isnumeric():
            continue
        while word.isalpha() != True:
            for thing in punctuation:
                word = word.replace(thing, '')
    result = []
    for word in textlist:
        if len(word) == number:
            result.append(word)
    print(result)


find_words_of_length(4, "this is a string with some four-letter words.")
    #>>> ['this', 'with', 'some']


#'four' in 'four-letter' is not considered a 4 letter word...?