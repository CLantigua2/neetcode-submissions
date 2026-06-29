# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        arr = []
        current = head
        while current:
            arr.append(current.val)
            current = current.next
        
        reversedHead = None

        for item in arr:
            reversedHead = ListNode(val=item, next=reversedHead)

        return reversedHead
        