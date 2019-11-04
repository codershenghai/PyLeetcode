class Solution(object):
    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 暴力法
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # hashtable
        ht = {}
        for i in range(len(nums)):
            ht[nums[i]] = i
        for j in range(len(nums)):
            if target-nums[j] in ht and j != ht[target-nums[j]]:
                return [j, ht[target-nums[j]]]


if __name__ == '__main__':
    Sol = Solution()
    res = Sol.twoSum2([3,2,4], 6)
    print(res)