from Py.Utils.Definition import ListNode


class Solution(object):
    def reverseList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 迭代：头插法
        dummy = ListNode(0)
        while head:
            q = head.next
            head.next = dummy.next
            dummy.next = head
            head = q
        return dummy.next

    def reverseList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 迭代：直接反插
        if not head or not head.next:
            return head
        pre = head
        p = pre.next
        r = p.next
        pre.next = None
        p.next = pre
        while r:
            pre = p
            p = r
            r = r.next
            p.next = pre
        return p

    def reverseList3(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 递归
        # 1.找终止条件。节点或下一个节点不存在时终止。
        # 2.找返回值。返回翻转后的链表。
        # 3.本级递归应该做什么。
        if not head or not head.next:
            return head
        p = self.reverseList3(head.next)
        head.next.next = head
        head.next = None
        return p


if __name__ == '__main__':
    head = ListNode(1)
    Sol = Solution()
    res = Sol.reverseList3(head)
    p = res
    while p:
        print(p.val)
        p = p.next
