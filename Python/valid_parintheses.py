def is_valid(str):
    print(type(str))
    stack = []
    dictionary = {")": "(", "}": "{", "]": "["}
    for char in str:
        if char not in dictionary:
            stack.append(char)
        else:
            if not stack:
                return False
            popped = stack.pop()
            if not popped == dictionary[char]:
                return False
    if stack:
        return False
    else:
        return True


print(is_valid("()[]{}"))

# The above uses a stack method to solve this problem. It loops over the string, adding opening brackets to the stack (by checking if the char is in the dictionary).
# Then, it checks 1. if the stack is empty, in which case it should return false.
# 2. if the popped element matches the value for dictionary[char]. If it doesn't, it returns false
# After the loop concludes, it checks if the stack is empty; if it isn't, it returns false, otherwise it returns true.
