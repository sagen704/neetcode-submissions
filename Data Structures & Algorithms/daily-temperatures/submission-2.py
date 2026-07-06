class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)

        stack = []

        for i in range(len(temperatures)):

            while len(stack) != 0 and temperatures[i] > stack[-1][0]:
                found_higher = stack.pop()
                # print(f"found higher {found_higher}")
                
                # updating the location
                res[found_higher[1]] = i - found_higher[1]
            stack.append([temperatures[i], i])

        return res
        