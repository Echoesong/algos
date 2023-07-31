# Okay so there are 2 main parts to this one:

# 1. Keeping track of the lowest value in the stack
# 2. Properly setting up the minStack class


class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        else:
            min = (
                self.stack[-1]
                if self.stack[-1] < self.min_stack[-1]
                else self.min_stack[-1]
            )
            self.min_stack.append(min)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin()
minStack.pop()
minStack.top()
minStack.getMin()
