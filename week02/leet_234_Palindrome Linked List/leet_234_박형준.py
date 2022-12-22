# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst = []
        while head != None:
            lst.append(head.val)
            head = head.next
        lst_l = len(lst)
        lst_l_2 = len(lst) // 2
        if lst_l % 2 == 0:
            if lst[:lst_l_2] == list(reversed(lst[lst_l_2:])):
                return True
            return False
        else:
            if lst[:lst_l_2] == list(reversed(lst[lst_l_2 + 1:])):
                return True
            return False

# 더 간략한 풀이


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q: Deque = collections.deque()
        while head != None:
            q.append(head.val)
            head = head.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        return True

# 런너 풀이


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev
