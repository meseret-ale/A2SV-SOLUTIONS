class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        
        nums.sort()
        j = len(nums) - 1
        ne = []
        for i in range(0, len(nums) // 2):
            total = nums[i] + nums[j]
            ne.append(total)
            total = 0
            j -= 1
        ne.sort()
        return ne[-1]

