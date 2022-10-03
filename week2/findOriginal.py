from collections import Counter
class Solution:
    
    def findOriginalArray(self, alist: List[int]) -> List[int]:
        
        if len(alist)%2 != 0:
            return  []
        
        count= Counter(alist)
        the_ans=[]
        alist.sort()
        
        for val in alist:
            
            if val == 0:
                if count[val] >= 2:
                    the_ans.append(val)
                    count[val] -= 2
                    
            else:
                if count[val] and count[val*2]:
                    count[val] -= 1
                    count[val*2] -= 1 
                    the_ans.append(val)
                    
        return the_ans if len(the_ans)== len(alist)//2 else []
            
