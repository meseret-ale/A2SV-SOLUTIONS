from collections import deque

class MyCircularDeque:

    def __init__(self, k: int):
        self.circular_queue = deque()
        self.length = k

    def insertFront(self, value: int) -> bool:
        if len(self.circular_queue)< self.length:
            self.circular_queue.appendleft(value)
            return True
        return False
        

    def insertLast(self, value: int) -> bool:
        if len(self.circular_queue)< self.length:
            self.circular_queue.append(value)
            return True
        return False
        
