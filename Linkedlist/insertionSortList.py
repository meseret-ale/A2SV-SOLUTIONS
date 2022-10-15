# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = end = head
        count = 0
        ls = []
        while start:
            count += 1
            ls.append(start.val)
            start = start.next
        lss = sorted(ls, reverse= True)
        m = 0
        while end:
            temp = head
            head = ListNode(lss[m])
            head.next = temp
            m += 1
            end = end.next
        c = 1
        ends = head
        while True:
            if c == count:
                ends.next = None
                break
            else:
                ends = ends.next
            c += 1
        return head
