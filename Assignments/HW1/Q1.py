def identify_consecutivity(string):
    consec = False
    if (string[0] == string[1]) and (string[2] == string[3]) and (string[4] == string[5]):
        return True
    else:
        return False


def trifeca(word):
    """Checks whether word contains three consecutive double-letter pairs.

    Parameters
    ----------
    word : string
        Input to check

    Returns
    -------
    result : bool
        True if three consecutive double-letter pairs were found,
        False otherwise
    """
    for i in range(len(word)-5):
        if identify_consecutivity(word[i:i+6]):
            return True
    return False
        

list_of_words = ['aabbcc', 'abccddee0123', 'llkkbm', 'aaaazz', 'bbcCdd', '', '1122']
for word in list_of_words:
    res = trifeca(word)
    print(f"Result for word {word} is {res}")