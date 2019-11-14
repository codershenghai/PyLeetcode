from Py.Utils.Definition import TreeNode


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 1.找终止条件。子树为空时终止。
        # 2.找返回值。返回当前树的最大深度。
        # 3.本级递归应该做什么。算出本级树的最大深度。
        if not root:
            return 0
        ldep = self.maxDepth(root.left)
        rdep = self.maxDepth(root.right)
        return max(ldep, rdep) + 1


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    Sol = Solution()
    print(Sol.maxDepth(root))
