# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
  
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, secondHalf = None, slow.next
        slow.next = None
        while secondHalf:
            nxt = secondHalf.next
            secondHalf.next = prev
            prev = secondHalf
            secondHalf = nxt

        while prev:
            nxt1, nxt2 = head.next, prev.next
            head.next = prev
            prev.next = nxt1
            head, prev = nxt1, nxt2


