from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        l1 = [2, 4, 3]
        l2 = [5, 6, 4]
        carry = 0

        Solution:
            1st: 
                total = 2 + 5 + 0 = 7
                carry = 7 // 10 = 0
                newList.next = ListNode(7 % 10) = ListNode(7)
            2st: 
                total = 4 + 6 + 0 = 10
                carry = 10 // 10 = 1
                newList.next = ListNode(10 % 10) = ListNode(0)
            3st:
                total = 3 + 4 + 1 = 8
                carry = 8 // 10 = 0
                newList.next = ListNode(8 % 10) = ListNode(8)
            
            output = List(7, 0, 8)
        """

        dummy: Optional[ListNode] = ListNode() # To keep the first node of Linked List
        current: Optional[ListNode] = dummy # Moving point for Linked List
        carry: int = 0

        while l1 or l2 or carry:
            v1: int = l1.val if l1 else 0
            v2: int = l2.val if l2 else 0

            total: int = v1 + v2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)

            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return dummy.next
