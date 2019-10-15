from Py.Utils.Definition import TreeNode


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 找终止条件：翻转一棵空树的结果还是一棵空树，因此当前节点不存在时返回None。
        # 找返回值：返回翻转后的二叉树。
        # 本级递归应该做什么：交换左子树和右子树。
        if not root:
            return None
        tmp = self.invertTree(root.left)
        root.left = self.invertTree(root.right)
        root.right = tmp
        return root


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    Sol = Solution()
    res = Sol.invertTree(root)
    print(res)