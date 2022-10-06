class MyQueue:
    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        vlu = self.queue.pop(0)
        return vlu
    def peek(self) -> int:
        vlu = self.queue[0]
        return vlu
    def empty(self) -> bool:
        if len(self.queue) == 0:
            return True
        return False
    
    
