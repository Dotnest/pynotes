def find_first_vowel(s: str) -> str:
    """ Return the first vowel in each word of a string.
    
    >>> find_first_vowel("The sky's the limit")
    'e, e, i'
    """

    # your code here
    result = []
    vowels = ('e', 'a', 'o', 'i', 'u')
    if s[-1] != " ":
        s += " "
    while s.find(' ') != -1:
        for i in range(s.find(' ')):
            #print(i, s.find(' '), s)
            if s[i] in vowels:
                result.append(s[i])
                s = s[s.find(' ')+1:]
                break
            if i == s.find(' ')-1:
                s = s[s.find(' ')+1:]
    print(result)



find_first_vowel("The sky's the limit")
find_first_vowel('This is a test of a little programm i made :)')