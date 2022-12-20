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
