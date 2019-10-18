class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 位运算
        res = 0
        for i in range(n.bit_length()):
            res += n & 1
            n >>= 1
        return res


if __name__ == '__main__':
    Sol = Solution()
    n = 0b0100000000000000000000000000000000001011
    print(n.bit_length())
    print(Sol.hammingWeight(n))