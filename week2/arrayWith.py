class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        alist=sorted(nums)
        for i in range(2, len(alist),2):
            alist[i], alist[i-1]=alist[i-1], alist[i]
        return alist
