from Py.Utils.Definition import ListNode


class Solution(object):
    def deleteDuplicates1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 迭代
        if not head:
            return None
        slow = head
        fast = head.next
        while fast:
            if fast.val == slow.val:
                p = fast
                fast = fast.next
                slow.next = fast
                del p
            else:
                fast = fast.next
                slow = slow.next
        return head

    def deleteDuplicates2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 递归
        # 1.找终止条件。当链表只剩一个元素的时候，当前节点和下一个节点有一个不存在则终止。
        # 2.找返回值。返回已删除重复元素的链表的头节点。
        # 3.本级递归应该做什么。从宏观上考虑，若head=head.next，则丢弃head，返回去重后的head.next。否则返回head。
        if not head or not head.next:
            return head
        if head.val == head.next.val:
            head = self.deleteDuplicates2(head.next)
        else:
            head.next = self.deleteDuplicates2(head.next)
        return head


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(3)
    Sol = Solution()
    res = Sol.deleteDuplicates2(head)

    p = res
    while p:
        print(p.val)
        p = p.next