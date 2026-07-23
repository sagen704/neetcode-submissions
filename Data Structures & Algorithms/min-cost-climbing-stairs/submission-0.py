class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # this is O(n) time and O(n) space where n is the length of cost

        steps = [0] * len(cost)

        steps[0], steps[1] = cost[0], cost[1]

        for i in range(2, len(cost)):
            # print(f"Checking step {cost[i]}")
            steps[i] = cost[i] + min(steps[i-1], steps[i-2])

        return min(steps[-1], steps[-2])
        