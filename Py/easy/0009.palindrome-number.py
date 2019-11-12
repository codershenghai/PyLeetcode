class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        cur = 0
        num = x
        while num:
            cur = cur * 10 + num % 10
            num //= 10
        return x == cur


if __name__ == '__main__':
    Sol = Solution()
    res = Sol.isPalindrome(1211)
    print(res)