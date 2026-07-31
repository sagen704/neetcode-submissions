class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        largest_rec = 0
        r = 0

        for i, h  in enumerate(heights):
            if not stack:
                stack.append([h,i])
                r += 1

            elif h > stack[-1][0]:
                stack.append([h,i])
                r += 1
            else:
                last_value = None
                while stack and h <= stack[-1][0]:
                    last_value = stack.pop()
                    area = last_value[0] * (r - last_value[1])
                    largest_rec = max(largest_rec, area)
                stack.append([h,last_value[1]])
                r += 1

        
        while stack:
            value = stack.pop()
            area = value[0] * (r - value[1])
            largest_rec = max(largest_rec, area)

        return largest_rec