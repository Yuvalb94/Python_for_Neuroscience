def is_palindrome(number):
    """
    Receive a number in type int or string, and check if it is a palindrome

    Returns True if the number is a palindrome, False otherwise
    """
    return str(number) == str(number)[::-1]


def check_palindrome():
    """Runs through all 6-digit numbers and checks the mentioned conditions.

    The function prints out the numbers that satisfy this condition.

    Notes
    -----
    It should print out the first number (with a palindrome in its last 4 digits),not all four "versions" of it.
    """
    for i in range(100000, 1000000):
        number_str = str(i)
        if is_palindrome(number_str[2:]):
            number_str = str(i + 1)
            if is_palindrome(number_str[1:]):
                number_str = str(i + 2)
                if is_palindrome(number_str[1:5]) and is_palindrome(i + 3):
                    print(i)
