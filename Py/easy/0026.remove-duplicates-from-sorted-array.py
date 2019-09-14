class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        for fast in range(1, len(nums)):
            if nums[low] == nums[fast]:
                fast += 1
            else:
                low += 1
                nums[low] = nums[fast]
        return low+1


if __name__ == '__main__':
    Sol = Solution()
    print(Sol.removeDuplicates([1, 1, 2]))