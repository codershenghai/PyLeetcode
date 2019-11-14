class Solution(object):
    def twoSum1(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 暴力法
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i]+numbers[j] == target:
                    return [i+1, j+1]

    def twoSum2(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # hashmap存储已访问过的数字
        visited = {}
        for index, number in enumerate(numbers):
            if target-number in visited:
                return [visited[target-number], index+1]
            else:
                visited[number] = index + 1

    def twoSum3(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 首尾指针
        i, j = 0, len(numbers)-1
        while i < j:
            if numbers[i]+numbers[j] == target:
                return [i+1, j+1]
            elif numbers[i]+numbers[j] > target:
                j -= 1
            else:
                i += 1


if __name__ == '__main__':
    Sol = Solution()
    print(Sol.twoSum3([2, 7, 11, 15], 9))
