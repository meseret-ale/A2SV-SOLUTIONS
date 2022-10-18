class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
      
        maxnum = 0
        start = 0
        zerocount = 0

        for i in range(0, len(nums)):
            if nums[i] == 0:
                zerocount += 1

            while zerocount > k:
                if nums[start] == 0:
                    zerocount -= 1
                start += 1

            maxnum = max(maxnum,i-start+1)
        return maxnum
