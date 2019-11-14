from typing import List


class Solution:
    def removeElement1(self, nums: List[int], val: int) -> int:
        # 将不需要删除的元素移到前面
        ans = 0
        for i in nums:
            if i != val:
                nums[ans] = i
                ans += 1
        return len(nums[:ans])

    def removeElement2(self, nums: List[int], val: int) -> int:
        # 直接把元素删除
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)


if __name__ == '__main__':
    Sol = Solution()
    res = Sol.removeElement2([3, 2, 2, 3], 3)
    print(res)