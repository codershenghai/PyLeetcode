class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 哈希表
        map = {}
        for i in nums:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
        res = []
        for key, value in map.items():
            if value > len(nums)//3:
                res.append(key)
        return res


if __name__ == '__main__':
    Sol = Solution()
    res = Sol.majorityElement([1,1,1,3,3,2,2,2])
    print(res)
