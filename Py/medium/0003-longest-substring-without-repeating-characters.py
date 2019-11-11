class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 滑动窗口
        # https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/hua-jie-suan-fa-3-wu-zhong-fu-zi-fu-de-zui-chang-z/
        n = len(s)
        ans = 0
        start = 0
        map = {}
        for end in range(n):
            alpha = s[end]
            if alpha in map:
                start = max(map[alpha], start)
            ans = max(ans, end-start+1)
            map[alpha] = end + 1
        return ans


if __name__ == '__main__':
    Sol = Solution()
    res = Sol.lengthOfLongestSubstring("abcabcbb")
    print(res)