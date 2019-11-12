class Solution:
    # 整数翻转，是9.回文数的基础
    def reverse(self, x: int) -> int:
        num = abs(x)
        cur = 0
        while num:
            cur = cur * 10 + num % 10
            num //= 10
        res = -cur if x < 0 else cur
        return res if -pow(2, 31) <= res <= pow(2, 31)-1 else 0


if __name__ == '__main__':
    Sol = Solution()
    res = Sol.reverse(1534236469)
    print(res)