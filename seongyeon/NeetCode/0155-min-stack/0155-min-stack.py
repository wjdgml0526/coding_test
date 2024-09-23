class MinStack(object):

    def __init__(self):
        self.st = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        min_val = self.getMin()
        if min_val == None or min_val > val:
            min_val = val
        
        self.st.append([val, min_val])

    def pop(self):
        """
        :rtype: None
        """
        self.st.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.st[-1][0] if self.st else None
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.st[-1][1] if self.st else None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()