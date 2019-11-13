from Py.Utils.Definition import ListNode


class Solution:
    # https://leetcode-cn.com/problems/merge-two-sorted-lists/solution/hua-jie-suan-fa-21-he-bing-liang-ge-you-xu-lian-bi/
    # 递归
    # 终止条件：当l1为空或l2为空时结束
    # 返回值：每一层调用都返回排序好的链表头
    # 本级递归内容：如果l1的val值更小，则将l1.next与排序好的链表头相接；l2同理
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next = ListNode(4)

    Sol = Solution()
    res = Sol.mergeTwoLists(l1, l2)
    while res:
        print(res.val)
        res = res.next