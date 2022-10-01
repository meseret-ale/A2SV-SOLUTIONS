class Solution:
    def smallerNumbersThanCurrent(self, nums):

        lis = []
        for i in range(0, len(nums)):
            count = 0
            for j in range(0, len(nums)):
                if nums[i] > nums[j]:
                    count += 1
            lis.append(count)

        return lis


lis = [8, 1, 2, 2, 3]
obj1 = Solution()
print(obj1.smallerNumbersThanCurrent(lis))
