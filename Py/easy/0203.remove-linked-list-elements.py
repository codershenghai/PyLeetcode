from Py.Utils.Definition import ListNode


class Solution(object):
    def removeElements1(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # 遍历链表，使用哑节点，不需为头结点特殊定制逻辑
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        p = head
        while p:
            if p.val == val:
                pre.next = p.next
                del p
                p = pre.next
            else:
                pre = pre.next
                p = p.next
        return dummy.next

    def removeElements2(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # 大神简化版，思想同上
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next

    def removeElements3(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # 递归
        if not head:
            return None
        head.next = self.removeElements3(head.next, val)
        if head.val == val:
            return head.next
        else:
            return head


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    Sol = Solution()
    res = Sol.removeElements3(head, val=3)

    p = res
    while p:
        print(p.val)
        p = p.next
