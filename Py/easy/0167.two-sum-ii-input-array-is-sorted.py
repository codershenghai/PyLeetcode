class Solution(object):
    def twoSum(self, numbers, target):
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


if __name__ == '__main__':
    Sol = Solution()
    print(Sol.twoSum([2,7,11,15], 9))
