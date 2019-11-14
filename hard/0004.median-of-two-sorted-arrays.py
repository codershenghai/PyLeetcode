class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # 暴力法（先排序，然后找中位数）
        unite = nums1 + nums2
        sorted_unite = sorted(unite)
        n = len(sorted_unite)
        if n % 2 == 0:
            res = (sorted_unite[n//2-1] + sorted_unite[n//2]) / 2
        else:
            res = sorted_unite[(n-1)//2]
        return res


if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3, 4]
    Sol = Solution()
    res = Sol.findMedianSortedArrays(nums1, nums2)
    print(res)