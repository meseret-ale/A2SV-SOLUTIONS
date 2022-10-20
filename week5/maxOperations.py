class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        
        count = 0
        i = 0
        m = len(nums)
        while len(nums):
            if len(nums) == 1:
                break
            j = 1
            l = 0
            while m > j:
                if nums[i] + nums[j] == k:
                    x = nums[j]
                    nums.remove(nums[i])
                    nums.remove(x)
                    count += 1
                    m -= 2
                    l += 1
                j += 1
            
            if l == 0:
                nums.remove(nums[0])
                m -= 1
                l = 0
                
        return count
