class Solution:
    def maxResult(self, nums, k):
        ans = [(0,-k)]

        for i in range(len(nums)):
            while i - ans[0][1] > k:
                heappop(ans)

            nums[i] -= ans[0][0]

            heapq.heappush(ans, (-nums[i],i))

        return nums[-1]
 
