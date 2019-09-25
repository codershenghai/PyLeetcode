class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits1(self, n):
        # 使用字符串
        return int(bin(n)[2:].zfill(32)[::-1], base=2)

    def reverseBits2(self, n):
        # 采用位运算，每次将原来的数字向左移动1位，
        # 就需要把该末尾加到我们的数字中去即可
        return 0


if __name__ == '__main__':
    Sol = Solution()
    print(Sol.reverseBits1(43261596))