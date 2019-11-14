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
        # 小顶堆的思想，维护一个大小为k的小顶堆，即保持堆顶元素是当前第k大的元素。
        import heapq
        return heapq.nlargest(k, nums)[-1]


class QS_Solution:
    def findKthLargest3(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 快排的思想，按从大到小确定pivot的位置。
        # 若pivot == k-1，则nums[pivot]即为答案。
        # 若pivot > k-1，则说明第k大的元素在pivot左边，继续在[left, pivot-1]中寻找。
        # 若pivot < k-1，则说明第k大的元素在pivot右边，继续在[pivot+1, right]中寻找。
        self.nums = nums
        self.k = k
        return self.select(0, len(nums)-1, k)

    def select(self, left, right, k):
        """
        :return: 返回第k大的数
        """
        # nums数组中只有一个数，直接返回这个数
        if left == right:
            return self.nums[left]

        # 找到pivot_index
        pivot_index = self.partition(left, right)

        if pivot_index < k-1:
            return self.select(pivot_index+1, right, k)
        elif pivot_index > k-1:
            return self.select(left, pivot_index-1, k)
        else:
            return self.nums[pivot_index]

    def partition(self, left, right):
        pivot = self.nums[left]
        while left < right:
            while left < right and self.nums[right] <= pivot:
                right -= 1
            self.nums[left] = self.nums[right]
            while left < right and self.nums[left] >= pivot:
                left += 1
            self.nums[right] = self.nums[left]
        self.nums[left] = pivot
        return left


if __name__ == '__main__':
    Sol = QS_Solution()
    res = Sol.findKthLargest3([3,2,1,5,6,4], k=2)
    print(res)