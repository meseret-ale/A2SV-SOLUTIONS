class Solution:
    def fib(self, n: int) -> int:
        
        if n < 2:
            return n
        firstnum = 0
        secondnum = 1
        temp = 0
        for i in range(1, n):
            temp = firstnum + secondnum
            firstnum = secondnum
            secondnum = temp
        return temp    
