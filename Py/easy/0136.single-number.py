class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """ 异或
        交换律：a ^ b ^ c <=> a ^ c ^ b
        任何数于0异或为任何数 0 ^ n => n
        相同的数异或为0: n ^ n => 0
        """

        res = 0
        for i in nums:
            res = res ^ i
        return res


if __name__ == '__main__':
    Sol = Solution()
    print(Sol.singleNumber([2,2,1]))
