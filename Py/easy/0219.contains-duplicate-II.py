class Solution(object):
    def containsNearbyDuplicate1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # 判断两个相等的数的下标的距离是否不超过k
        # 线性滑动窗口（超时）
        for i in range(len(nums)):
            for j in range(1, k+1):
                if i+j < len(nums) and nums[i] == nums[i+j]:
                    return True
        return False

    def containsNearbyDuplicate2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # 判断两个相等的数的下标的距离是否不超过k
        # 哈希表滑动窗口
        window = set()
        for i in range(len(nums)):
            if nums[i] in window:
                return True
            window.add(nums[i])
            if len(window) > k:
                window.remove(nums[i-k])
        return False


if __name__ == '__main__':
    Sol = Solution()
    res = Sol.containsNearbyDuplicate2([1,2,3,1,2,3], 2)
    print(res)