class Solution(object):
    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 暴力法
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j]-prices[i] > max_profit:
                    max_profit = prices[j]-prices[i]
        return max_profit

    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 找最低的买入点
        max_profit = 0
        min_price = float('inf')
        for i in prices:
            if i < min_price:
                min_price = i
            elif i - min_price > max_profit:
                max_profit = i - min_price
        return max_profit


if __name__ == '__main__':
    Sol = Solution()
    print(Sol.maxProfit1([7, 1, 5, 3, 6, 4]))