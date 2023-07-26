import re


def is_palindrome(str):
    str.lower()
    clean_str = []
    test = r"[a-zA-Z]"
    for char in str:
        if bool(re.match(test, char)):
            clean_str.append(char)
    print(clean_str)
    reverse_string = []
    for char in clean_str:
        shift = clean_str.pop()
        reverse_string.append(shift)

    print(reverse_string)


is_palindrome("A man, a plan, a canal: Panamaz")
