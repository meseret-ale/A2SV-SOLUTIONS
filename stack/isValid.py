
from collections import deque
class Solution:
    def isValid(self, s):

        stack = deque()
        print(stack)
        my_dict = {"}": "{", ")": "(", "]": "["}

        for par in s:

            print(stack)
            if par in my_dict:
                if stack and my_dict[par] == stack[-1]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(par)

        return True if not stack else False

obj1 = Solution()
print(obj1.isValid("({})"))
