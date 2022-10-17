class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        the_dict = {}
        monoStack = []
        
        for val in nums2:
            if len(monoStack) == 0:
                monoStack.append(val)
            else:
                if val <= monoStack[-1]:
                    monoStack.append(val)
                else:
                    while monoStack and val > monoStack[-1]:
                        the_dict[monoStack[-1]] = val
                        monoStack.pop()
                    monoStack.append(val)
        
        ans =[]
        
        for item in nums1:
            if item in the_dict:
                ans.append(the_dict[item])
            else:
                ans.append(-1)
                
        return ans
                
                        
                    
