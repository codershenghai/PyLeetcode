from Py.Utils.Definition import ListNode


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = l2
        cur = dummy
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum = x + y + carry
            carry = sum // 10
            cur.next = ListNode(sum % 10)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry:
            cur.next = ListNode(carry)
        return dummy.next


if __name__ == '__main__':
    l1 = ListNode(5)
    # l1.next = ListNode(4)
    # l1.next.next = ListNode(3)

    l2 = ListNode(5)
    # l2.next = ListNode(6)
    # l2.next.next = ListNode(4)

    Sol = Solution()
    res = Sol.addTwoNumbers(l1, l2)

    print(res)