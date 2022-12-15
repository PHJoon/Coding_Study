class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = prices[:]
        now_p = [0] * len(prices)
        for i in range(1, len(prices)):
            min_p[i] = min(prices[i], min_p[i - 1])
            now_p[i] = prices[i] - min_p[i - 1]
        return max(now_p)
