# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        length = 0
        start = end = head
        while start:
            length += 1
            start = start.next
        
        n = length // 2
        for i in range(0, length):
            if i >= n:
                return end
            else:
                end = end.next
        
        return None
