class Solution(object):
    def moveZeroes1(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 一个index记录位置，另一个index记录0的个数。
        index = 0
        zeros = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[index] = nums[i]
                index += 1
            else:
                zeros += 1
        for i in range(index, index + zeros):
            nums[i] = 0
        return nums

    def moveZeroes2(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 快慢指针
        slow = fast = 0
        while fast < len(nums):
            if nums[fast] != 0:
                tmp = nums[fast]
                nums[fast] = nums[slow]
                nums[slow] = tmp
                slow += 1
            fast += 1
        return nums


if __name__ == '__main__':
    Sol = Solution()
    res = Sol.moveZeroes2([0,1,0,3,12])
    print(res)