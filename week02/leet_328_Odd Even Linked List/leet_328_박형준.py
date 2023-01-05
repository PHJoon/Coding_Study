# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = tmp = ListNode(0)
        vals = []
        while (head):
            vals.append(head.val)
            head = head.next
        vlen = len(vals)
        for i in range(0, vlen, 2):
            tmp.next = ListNode(vals[i])
            tmp = tmp.next
        for i in range(1, vlen, 2):
            tmp.next = ListNode(vals[i])
            tmp = tmp.next

        return root.next
