class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        
        num = [int(i) for i in nums]
        res = sorted(num, reverse = True)
        
        return str(res[k - 1])
