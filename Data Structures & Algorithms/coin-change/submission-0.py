class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        res = [0]
        # print(res)

        for i in range(1, amount+1):
            num_coins = []
            for j in range(len(coins)):
                if 0 <= i - coins[j] <= i and res[i - coins[j]] != -1:
                    num_coins.append(1 + res[i - coins[j]])

            if num_coins:
                res.append(min(num_coins))
            else:
                res.append(-1)
            # print(res)

        return res[-1]
        