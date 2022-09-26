class Solution(object):
    def fizzBuzz(self, n):
        set1 = []
        for i in range(1, n+1):
            if ((i %3 == 0) & (i%5 == 0)):
                set1.append("fizzbuzz")
                
            elif i % 3 == 0:
                set1.append("fizz")
                   
            elif i % 5 == 0:
                set1.append("buzz")
                
            else:
                set1.append(str(i))
        return set1
                                                                                            

fizzbuzz1 =  Solution()
s = fizzbuzz1.fizzBuzz(15)
print(s)
