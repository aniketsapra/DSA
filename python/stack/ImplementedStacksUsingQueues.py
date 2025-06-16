#easy
#stack

from collections import deque

class MyStack(object):

    def __init__(self):
        self.stack = deque()

    def push(self, x):
        return self.stack.append(x)

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def empty(self):
        return not self.stack
 
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()