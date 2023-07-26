def isPalindrome(nums):
    y = str(nums)
    reverse = y[::-1]
    if y == reverse:
        return True
    else:
        return False


x = 121

isPalindrome(x)

# The above changes the number into a string, then reverses it by using Python's slice operation to iterate over the array backwards. then it's a simple matter of comparison
