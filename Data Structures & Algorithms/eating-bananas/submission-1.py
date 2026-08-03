class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)

        while l <= r:
            m = (r+l) // 2
            time_taken = 0

            for pile in piles:
                time_taken += math.ceil(pile / m)

            # print(f"Eating at {m} = {time_taken}")

            if time_taken <= h:
                r = m - 1
            else:
                l = m + 1

        # print(l,r)

        return l