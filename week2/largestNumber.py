class Solution():
    def largestNumber(self, alist: List[int]) -> str:
        
         for passnum in range(len(alist)-1,0,-1):
            for index in range(passnum):
                if int(str(alist[index])+str(alist[index+1]))<int(str(alist[index+1])+str(alist[index])):
                    alist[index], alist[index+1]=alist[index+1], alist[index]
         return str(int("".join([str(n) for n in alist])))
