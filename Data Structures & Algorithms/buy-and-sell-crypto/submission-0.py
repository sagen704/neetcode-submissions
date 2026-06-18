class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_proffit = 0

        current_bid = prices[0]

        for i in range(len(prices)):

            if prices[i] < current_bid:
                current_bid = prices[i]
            if prices[i] - current_bid > max_proffit:
                max_proffit = prices[i] - current_bid

        return max_proffit