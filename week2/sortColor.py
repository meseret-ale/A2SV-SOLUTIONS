class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    
        r = 0
        w = 0
        b = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                r += 1
            elif nums[i] == 1:
                w += 1
            elif nums[i] == 2:
                b += 1
        for i in range(r):
            nums[i] = 0
        for i in range(r, r + w):
            nums[i] = 1
        for i in range(r + w, r + w + b):
            nums[i] = 2
