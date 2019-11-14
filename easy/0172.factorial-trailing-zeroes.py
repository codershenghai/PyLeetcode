class Solution(object):
    def trailingZeroes1_1(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 求解这个数字分解质因数之后一共有多少个5
        # f(n) = n/5 + n/5^2 + n/5^3 + n/5^4 + n/5^5 + ...
        # 循环实现1
        if n == 0:
            return 0
        import math
        fn = 0
        for i in range(1, int(math.log(n, 5))+1):
            fn += int(n/(5**i))
        return fn

    def trailingZeroes1_2(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 求解这个数字分解质因数之后一共有多少个5
        # f(n) = n/5 + n/5^2 + n/5^3 + n/5^4 + n/5^5 + ...
        # 循环实现2
        count = 0
        while n >= 5:
            n = n//5
            count += n
        return count

    def trailingZeroes2(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 求解这个数字分解质因数之后一共有多少个5
        # f(n) = n/5 + n/5^2 + n/5^3 + n/5^4 + n/5^5 + ...
        # 递归实现
        if n == 0:
            return 0
        return n//5 + self.trailingZeroes2(n//5)


if __name__ == '__main__':
    import math
    Sol = Solution()
    print(Sol.trailingZeroes2(31))