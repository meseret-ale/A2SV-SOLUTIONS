import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        

        stack = []
        sums = 0
        lis = ["-", "+", "/", "*"]
        if len(tokens) == 1:
            sums = int(tokens[0])
            
        for token in tokens:
            if token in lis:

                firstnum = int(stack.pop())
                secondnum = int(stack.pop())
                if token == "-":
                    sums = secondnum - firstnum
                    stack.append(sums)
                elif token == "+":
                    sums = secondnum + firstnum
                    stack.append(sums)
                elif token == "/":
                    sums = int(secondnum / firstnum)
                    stack.append(sums)
                elif token == "*":
                    sums = secondnum * firstnum
                    stack.append(sums)

            else:
                stack.append(token)

        return sums
