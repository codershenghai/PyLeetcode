class Solution(object):
    def isPowerOfFour1(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # 递归
        if num == 0:
            return False
        if num != 1:
            if num % 4 == 0:
                return self.isPowerOfFour1(num/4)
            else:
                return False
        return num == 1

    def isPowerOfFour2(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # 循环
        if num == 0:
            return False
        while num % 4 == 0:
            num /= 4
        return num == 1


if __name__ == '__main__':
    Sol = Solution()
    res = Sol.isPowerOfFour2(0)
    print(res)