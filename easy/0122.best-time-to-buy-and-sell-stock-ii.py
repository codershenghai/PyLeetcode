class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 一次遍历(贪心算法)
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i]-prices[i-1] > 0:
                max_profit += prices[i]-prices[i-1]
        return max_profit


if __name__ == '__main__':
    Sol = Solution()
    print(Sol.maxProfit([7,6,4,3,1]))