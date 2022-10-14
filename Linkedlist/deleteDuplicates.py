# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        else:
            current = head
            while True:
                nextvalu = current.next
                if nextvalu is None:
                    break
                if current.val == nextvalu.val:
                    if nextvalu.next is None:
                        current.next = None
                        break
                    current.next = nextvalu.next
                else:

                    current = current.next
        
        return head
            
