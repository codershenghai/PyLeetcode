class MinStack(object):
    # 使用python栈的特性
    def __init__(self):
        self.data = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.data.append(x)

    def pop(self):
        """
        :rtype: None
        """
        self.data.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.data)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


if __name__ == '__main__':
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin())
    obj.pop()
    print(obj.top())
    print(obj.getMin())