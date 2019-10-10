from Py.Utils.Definition import TreeNode


class Solution(object):
    # 1.找终止条件。子树为空的时候递归终止。
    # 2.找返回值。子树是否是平衡二叉树以及子树的深度。可以单独定义一个ReturnNode类。
    # 3.本级递归应该做什么。判断左、右子树是否都为平衡二叉树，若是则判断深度是否不大于1，如果不大于1则返回True和深度，否则返回False和深度；
    #   若左右子树有一个不是平衡二叉树，则直接返回False和深度-1。
    class ReturnNode:
        def __init__(self, isB, depth):
            self.isB = isB
            self.depth = depth

    def helper(self, root):
        if not root:
            return self.ReturnNode(True, 0)
        left = self.helper(root.left)
        right = self.helper(root.right)
        if not left.isB or not right.isB:
            return self.ReturnNode(False, -1)
        else:
            if abs(left.depth-right.depth) > 1:
                return self.ReturnNode(False, -1)
            else:
                return self.ReturnNode(True, max(left.depth, right.depth)+1)

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root).isB


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    # root.left.left.left = TreeNode(5)
    Sol = Solution()
    print(Sol.isBalanced(root))