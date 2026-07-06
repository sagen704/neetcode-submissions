class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)

        stack = []

        for i in range(len(temperatures)):

            if not stack:
                stack.append([temperatures[i], i])
                
            # add it if it is decreasing or equal
            elif temperatures[i] <= stack[-1][0]:
                stack.append([temperatures[i], i])
                
            # remove if it is higher or equal
            else:
                while len(stack) != 0 and temperatures[i] > stack[-1][0]:
                    found_higher = stack.pop()
                    print(f"found higher {found_higher}")
                    
                    # updating the location
                    res[found_higher[1]] = i - found_higher[1]
                stack.append([temperatures[i], i])
                
        return res
        