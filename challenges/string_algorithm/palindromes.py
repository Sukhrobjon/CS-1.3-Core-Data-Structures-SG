#!python
import re
import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):

    # normalize the string and remove all punctuation and whitespaces
    text = re.sub('[^A-Za-z0-9]+', '', text.lower())

    last_index = len(text) - 1 
    for i in range(len(text)//2):
        if text[i] != text[last_index-i]:
            return False
    return True
    


def is_palindrome_recursive(text, left=None, right=None):
    
    # normalize the string and remove all punctuation and whitespaces
    text = re.sub('[^A-Za-z0-9]+', '', text.lower())

    if left == None and right == None:
        left = 0
        right = len(text) - 1

    if left >= right:
        return True

    elif text[left] == text[right]:
        return is_palindrome_recursive(text, left + 1, right -1)
    
    return False

    


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()

