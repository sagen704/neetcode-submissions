class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        largest_rec = 0
        r = 0

        for i, h  in enumerate(heights):
            if not stack:
                print(f"adding {[h,i]} to stack")
                stack.append([h,i])
                r += 1

            elif h > stack[-1][0]:
                print(f"adding {[h,i]} to stack")
                stack.append([h,i])
                r += 1
            else:
                last_value = None
                while stack and h <= stack[-1][0]:
                    last_value = stack.pop()
                    print(f"removing {last_value} from stack")
                    area = last_value[0] * (r - last_value[1])
                    largest_rec = max(largest_rec, area)
                print(f"adding {[h,last_value[1]]} to stack, last val is {last_value}, area = {largest_rec}")
                stack.append([h,last_value[1]])
                r += 1

        
        while stack:
            value = stack.pop()
            area = value[0] * (r - value[1])
            largest_rec = max(largest_rec, area)
            print(f"removing {value} from stack")

        print(f"largest_rec = {largest_rec}")

        return largest_rec