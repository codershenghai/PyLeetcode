class Solution:
    def romanToInt(self, s: str) -> int:
        # 首先在hashmap中找两个字符对应的数字，没有的话再找一个字符对应的数字
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
               'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        res, i = 0, 0
        while i < len(s):
            if s[i:i+2] in dic:
                res += dic[s[i:i+2]]
                i += 2
            else:
                res += dic[s[i]]
                i += 1
        return res


if __name__ == '__main__':
    Sol = Solution()
    res = Sol.romanToInt("III")
    print(res)