class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 先处理字符串，然后使用头尾指针
        s = ''.join(i for i in s if i.isalnum()).lower()
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == '__main__':
    Sol = Solution()
    str = "race a car"
    print(Sol.isPalindrome(str))