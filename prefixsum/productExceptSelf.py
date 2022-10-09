class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodact = 1
        m = 0

        for i in range(0, len(nums)):
            if nums[i] == 0:
                m += 1
                continue
            prodact *= nums[i]

        lis = []
        if m > 0:
            if m == 1:
                for i in range(0, len(nums)):
                    if nums[i] == 0:
                        lis.append(prodact)
                        continue
                    lis.append(0)

            elif m > 1:
                lis = [0] * len(nums)

        else:
            lis = [int(prodact / i) for i in nums if i != 0]

        return lis
