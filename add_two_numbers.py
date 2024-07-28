from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        response = ListNode(0)
        current = response
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            result = l1_val + l2_val + carry
            carry = result // 10
            new_node = ListNode(result % 10)
            current.next = new_node
            current = new_node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return response.next


if __name__ == '__main__':
    print(Solution().addTwoNumbers(l1, l2))
