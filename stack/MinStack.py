class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
    
    def pop(self) -> None:
        p = self.stack.pop()
        return p
    
    def top(self) -> int:
        s = self.stack[-1]
        return s
    
    def getMin(self) -> int:
        
        s = 0
        for i in range(0, len(self.stack)-1):
            if s > self.stack[i]:
                s = self.stack[i]
        
        return s
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
