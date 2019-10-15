from Py.Utils.Definition import TreeNode


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        # 1.找终止条件。当t1和t2都不存在时，返回None。
        # 2.找返回值。(1)当t1和t2都存在时，把t2的值加到t1上，返回t1。
        #           (2)当t1存在，t2不存在时，返回t1。
        #           (3)当t2存在，t1不存在时，返回t2。
        # 3.本级递归应该做什么。判断t1和t2的存在情况，根据存在情况递归。
        if not t1 and not t2:
            return None
        if not t2:
            return t1
        if not t1:
            return t2
        if t1 and t2:
            t1.val += t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
            return t1


if __name__ == '__main__':
    t1 = TreeNode(1)
    t1.left = TreeNode(3)
    t1.right = TreeNode(2)
    t1.left.left = TreeNode(5)

    t2 = TreeNode(2)
    t2.left = TreeNode(1)
    t2.right = TreeNode(3)
    t2.left.right = TreeNode(4)
    t2.right.right = TreeNode(7)

    Sol = Solution()
    res = Sol.mergeTrees(t1, t2)
    print(res)