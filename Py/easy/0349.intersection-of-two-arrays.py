class Solution(object):
    def intersection1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # python列表推导式
        return list(set([x for x in nums1 if x in nums2]))

    def intersection2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # python集合
        return set(nums1) & set(nums2)

    def intersection3(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # hashtable
        visited, result = {}, []
        for i in nums1:
            visited[i] = i
        for i in nums2:
            if i in visited:
                result.append(i)
                visited.pop(i)
        return result


if __name__ == '__main__':
    Sol = Solution()
    res = Sol.intersection3([4,9,5], [9,4,9,8,4])
    print(res)