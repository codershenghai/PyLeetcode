class Solution(object):
    def maxSubArray1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 暴力法
        max_sum = float('-inf')
        for i in range(len(nums)+1):
            for j in range(i+1, len(nums)+1):
                subArr_sum = sum(nums[i: j])
                if subArr_sum > max_sum:
                    max_sum = subArr_sum
        return max_sum

    def maxSubArray2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 分治法
        def helper(nums, l, r):
            if l > r:
                return float('-inf')
            mid = (l + r) // 2

            # 不考虑中间元素, 最大子序列出现在左半部分
            left_max = helper(nums, l, mid-1)

            # 不考虑中间元素, 最大子序列出现在右半部分
            right_max = helper(nums, mid+1, r)

            # 考虑中间元素, 向左求出后缀最大, 向右求出后缀最大, 并连接
            left_suffix_max_sum = right_suffix_max_sum = 0
            tmp_sum = 0
            for i in reversed(range(l, mid)):
                tmp_sum += nums[i]
                left_suffix_max_sum = max(tmp_sum, left_suffix_max_sum)
            tmp_sum = 0
            for i in range(mid+1, r+1):
                tmp_sum += nums[i]
                right_suffix_max_sum = max(tmp_sum, right_suffix_max_sum)
            cross_max = left_suffix_max_sum + right_suffix_max_sum + nums[mid]
            return max(left_max, right_max, cross_max)

        return helper(nums, 0, len(nums)-1)

    def maxSubArray3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 动态规划
        cur_max_sum = max_sum = nums[0]
        for i in range(1, len(nums)):
            cur_max_sum = max(cur_max_sum+nums[i], nums[i])
            max_sum = max(cur_max_sum, max_sum)
        return max_sum


if __name__ == '__main__':
    import time
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    Sol = Solution()
    start = time.time()
    print(time.time())
    print(Sol.maxSubArray3(arr))
    print("运行时间: %.3f秒" % (time.time()-start))