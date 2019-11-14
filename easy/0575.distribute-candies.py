class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        # 如果糖果种类大于n/2，妹妹最多可以获得的糖果种类是n/2(因为妹妹只有n/2个糖果)。
        # 如果糖果种类小于n/2，妹妹最多可以获得的糖果种类是糖果的种类数(每种糖都至少给了妹妹一个)。
        # 使用集合可以得到糖果的种类数(考虑唯一性的时候，多考虑set)。
        return min(len(set(candies)), len(candies)//2)


if __name__ == '__main__':
    Sol = Solution()
    res = Sol.distributeCandies([1, 2, 1, 1, 1, 1])
    print(res)


