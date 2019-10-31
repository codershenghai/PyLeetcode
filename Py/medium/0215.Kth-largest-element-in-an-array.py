class Solution(object):
    def findKthLargest1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 暴力
        return sorted(nums)[-k]

    def findKthLargest2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 小顶堆的思想，维护一个大小为k的小顶堆，即保持堆顶元素是当前第k小的元素。
        import headq
        pq = PQ()
        for i in nums:
            pq.put(i)
            if pq.qsize() > k:
                pq.get()
        return pq.get()


if __name__ == '__main__':
    Sol = Solution()
    res = Sol.findKthLargest2([3,2,1,5,6,4], k=2)
    print(res)