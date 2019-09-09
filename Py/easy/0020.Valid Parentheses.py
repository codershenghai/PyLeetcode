class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 使用栈的思想
        stack = []
        dic = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for i in s:
            if i in dic.keys():
                stack.append(i)
            else:
                if len(stack) != 0:
                    top = stack.pop()
                    if i != dic[top]:
                        return False
                else:
                    return False
        return len(stack) == 0


if __name__ == '__main__':
    Sol = Solution()
    print(Sol.isValid("{"))