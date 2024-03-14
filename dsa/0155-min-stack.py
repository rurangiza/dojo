# Date: 03/11/2023

"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
"""

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minimum = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)

        if not self.minimum or val < self.minimum[-1]:
            self.minimum.append(val)
        else:
            self.minimum.append(self.minimum[-1])

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minimum.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self):
        """
        :rtype: int
        """
        return self.minimum[-1]

#############################################

def main():
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.stack)
    obj.pop()
    print(obj.stack)
    param_3 = obj.top()
    print("param_3", param_3)
    print(obj.minimum)
    param_4 = obj.getMin()
    print("param_4 (minimum)", param_4)

if __name__ == "__main__":
    main()