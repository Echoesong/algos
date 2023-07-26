import re


def is_palindrome(str):
    str = str.lower()
    clean_str = []
    test = r"[a-zA-Z0-9]"
    for char in str:
        if bool(re.match(test, char)):
            clean_str.append(char)
    print(clean_str)
    reverse_string = clean_str[::-1]
    if clean_str == reverse_string:
        return True
    else:
        return False


print(is_palindrome("0P"))

# T EFFICIENCY: O(n)
# S EFFICIENCY: O(n)
