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
        return


    def Partition(a, low, high):
        pivot = a[low]
        while low < high:
            while low < high and a[high] >= pivot:
                high -= 1
            a[low] = a[high]
            while low < high and a[low] <= pivot:
                low += 1
            a[high] = a[low]
        a[low] = pivot
        return low

    def select(self, nums, left, right, k):
        pivot = left
        if left < right:
            pivot = Partition(nums, left, right)
            if pivot < k-1:
                self.findKthLargest3(nums, left, pivot-1)
            elif pivot > k-1:
                self.findKthLargest3(nums, pivot+1, right)
            else:
                return nums[pivot]


if __name__ == '__main__':
    Sol = Solution()
    res = Sol.findKthLargest3([3,2,1,5,6,4], k=2)
    print(res)