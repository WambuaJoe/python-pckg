def count_vowels(word):
    """
    Given a single word, return the total number of vowels in that single word.

    :param word: str
    :return: int

    >>> count_vowels('Cusco')
    2

    >>> count_vowels('Manila')
    3
    >>> count_vowels('Islamabad')
    4
    >>> count_vowels('Chernobyl')
    3
    """
    total_vowels = 0
    for letter in word.lower():
        if letter in 'aeiou':
            total_vowels += 1
    return total_vowels


if __name__ == "__main__":
    import doctest
    doctest.testmod(name='count_vowels', verbose=True)