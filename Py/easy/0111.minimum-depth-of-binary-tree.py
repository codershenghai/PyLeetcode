from Py.Utils.Definition import TreeNode


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:  # root不存在
            return 0
        elif root.left and root.right:  # root的左右子树都存在
            return min(self.minDepth(root.left), self.minDepth(root.right))+1
        elif root.left and not root.right:  # root的左子树存在，右子树不存在
            return self.minDepth(root.left)+1
        elif not root.left and root.right:  # root的左子树不存在，右子树存在
            return self.minDepth(root.right)+1
        else:  # root的左右子树都不存在，但root存在
            return 1


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(6)
    Sol = Solution()
    print(Sol.minDepth(root))
