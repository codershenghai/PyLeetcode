class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # 将给定数字除以2、3、5(顺序无所谓)，直到无法整除。
        # 若结果为1，则说明所有的因子都是2或3或5，给定数字是丑数。
        # 否则，给定数字不是丑数。
        if num <= 0:
            return False
        for i in [2, 3, 5]:
            while num % i == 0:
                num /= i
        return num == 1


if __name__ == '__main__':
    Sol = Solution()
    res = Sol.isUgly(0)
    print(res)