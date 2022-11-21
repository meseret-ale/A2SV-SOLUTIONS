"""The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,"""

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
