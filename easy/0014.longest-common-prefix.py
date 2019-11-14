from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 两两比较，找出最长公共前缀
        # https://leetcode-cn.com/problems/longest-common-prefix/solution/hua-jie-suan-fa-14-zui-chang-gong-gong-qian-zhui-b/
        if len(strs) == 0:
            return ""
        cur = strs[0]
        for i in range(1, len(strs)):
            for j in range(len(strs[i])+1):
                if j < len(cur) and j < len(strs[i]) and cur[j] != strs[i][j]:
                    break
            cur = cur[0:j]
        return cur


if __name__ == '__main__':
    Sol = Solution()
    res = Sol.longestCommonPrefix(["a", "a"])
    print(res)