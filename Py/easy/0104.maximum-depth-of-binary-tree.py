from Py.Utils.Definition import TreeNode


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
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
