class Solution:
    def maxArea(self, height: List[int]) -> int:
        pairs = []
        for i, val in enumerate(height):
            pairs.append((i, val))
            
        l = 0 
        h = len(height)-1
        area = 0
        
        while l < h:
            left = pairs[l]
            right = pairs[h]
            
            if left[1] < right[1]:
                area = max(area, (right[0]-left[0])* min(left[1], right[1]))
                l += 1
            elif left[1] > right[1]:
                area = max(area, (right[0]-left[0])*min(left[1], right[1]))
                h -= 1
            else:
                area = max(area, (right[0]-left[0])*min(left[1], right[1]))
                l += 1
                h -= 1
        return area
        
            
