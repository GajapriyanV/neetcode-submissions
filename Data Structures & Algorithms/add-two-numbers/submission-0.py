class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 and l2:
            
            total = l1.val + l2.val + carry
            remain = total % 10
            carry = total // 10

            cur.next = ListNode(remain)
            cur = cur.next

            l1 = l1.next
            l2 = l2.next
        
        while l1:
            total = l1.val + carry
            remain = total % 10
            carry = total // 10

            cur.next = ListNode(remain)
            cur = cur.next

            l1 = l1.next
        
        while l2:
            total = l2.val + carry
            remain = total % 10
            carry = total // 10

            cur.next = ListNode(remain)
            cur = cur.next

            l2 = l2.next
        
        if carry:
            cur.next = ListNode(carry)
        
        return dummy.next