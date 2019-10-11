from Py.Utils.Definition import TreeNode


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 直接造个新的树与自己比较！
        # 什么时候为对称二叉树？(1)根节点有相同的值。(2)每个树的右子树与另一个树的左子树镜像对称。
        # 1.找终止条件。两个二叉树都为空时返回True，只有一个为空时返回False。
        # 2.找返回值。返回子树是否为对称二叉树。
        # 3.本级递归应该做什么。(1)判断根节点的值是否相等。
        #                    (2)判断A的右子树和B的左子树是否对称。
        #                    (3)判断A的左子树和B的右子树是否对称。
        return self.helper(root, root)

    def helper(self, t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return t1.val == t2.val and self.helper(t1.left, t2.right) and self.helper(t1.right, t2.left)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    Sol = Solution()
    print(Sol.isSymmetric(root))