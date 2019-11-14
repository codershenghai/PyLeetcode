class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits1(self, n):
        # 使用字符串
        return int(bin(n)[2:].zfill(32)[::-1], base=2)

    def reverseBits2(self, n):
        # 采用位运算，设置一个变量res，在每次循环中，
        # res左移一位，然后加上n的最后一位的值，然后n右移一位，
        # 这样可以保持res和n既同步又相反
        res = 0
        for i in range(32):
            res <<= 1
            # 把n与1进行与运算，得到n的最低位
            res += n & 1
            n >>= 1
        return int(bin(res), 2)


if __name__ == '__main__':
    Sol = Solution()
    print(Sol.reverseBits2(4))