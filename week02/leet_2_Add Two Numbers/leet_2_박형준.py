# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def len_listnode(lst):
            cnt = 1
            if lst == None:
                return 0
            while (lst.next):
                cnt += 1
                lst = lst.next
            return cnt

        len1 = len_listnode(l1)
        len2 = len_listnode(l2)
        if len1 == 0:
            return l2
        elif len2 == 0:
            return l1
        flag = 0
        if (len1 > len2):
            tmp1 = l1
            tmp2 = l2
        else:
            tmp1 = l2
            tmp2 = l1

        while tmp1:
            if tmp2:
                tmp1.val += tmp2.val + flag
                if tmp1.val >= 10:
                    flag = 1
                    tmp1.val -= 10
                else:
                    flag = 0
                tmp2 = tmp2.next
            else:
                tmp1.val += flag
                if tmp1.val >= 10:
                    flag = 1
                    tmp1.val -= 10
                else:
                    flag = 0

            if not tmp1.next:
                if flag == 1:
                    tmp1.next = ListNode(0, None)

            tmp1 = tmp1.next

        if (len1 > len2):
            return l1
        else:
            return l2

# 더 깔끔한 풀이
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            sum = 0

            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next
        return root.next
