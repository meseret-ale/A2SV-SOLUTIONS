# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        len_linkedlist = 0
        start = end = head
        
        while start:
            len_linkedlist += 1
            start = start.next
        
        
        middel = len_linkedlist // 2
        
        count = 0
        while end:
            if count == middel:
                return end
            else:
                count+=1
                end = end.next
        
        return None
            
