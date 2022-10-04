class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        sor = sorted(nums)
        m = 0
        
        for i in range(0, len(sor)):
            for j in range(i + 1, len(sor)):
                if sor[i] == sor[j]:
                    m += 1
        return m
