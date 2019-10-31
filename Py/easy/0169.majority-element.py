class Solution(object):
    def majorityElement1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 哈希表记录每个元素出现的次数
        map = {}
        for i in nums:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
        return max(map, key=map.get)

    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 投票算法。
        # 假设majority出现的次数是m, 总元素个数是N，最终剩余的majority个数就是m-(N-m), 即2m-N。
        # 所以必须是m > ⌊N/2⌋时才有效。
        vote = 0
        majority = nums[0]
        for i in range(len(nums)):
            if nums[i] == majority:
                vote += 1
            else:
                vote -= 1
                if vote == 0:
                    majority = nums[i+1]
        return majority

    def majorityElement3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 由于majority个数大于⌊N/2⌋,
        # 所以先进行排序, 然后输出⌊N/2⌋位置的数即为majority
        return sorted(nums)[len(nums)//2]


if __name__ == '__main__':
    Sol = Solution()
    print(Sol.majorityElement2([2,2,1,1,1,2,2,1,1]))