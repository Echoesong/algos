# Okay so there are 2 main parts to this one:

# 1. Keeping track of the lowest value in the stack
# 2. Properly setting up the minStack class


class MinStack(object):
    def __init__(self):
        self.stack = []
        self.lowest = None
        self.next_lowest = None

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        # Add the value to self
        self.stack.append(val)
        if val <= self.lowest:
            self.next_lowest = self.lowest
            self.lowest = val

    def pop(self):
        """
        :rtype: None
        """
        # Remove the last value from self
        if self.stack[-1] == self.lowest:
            self.lowest = self.next_lowest
            self.next_lowest = None
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        # Return the last value from self, do not remove it
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        # Return lowest value element in self
        return self.lowest


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
