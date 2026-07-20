class Solution:
    def trap(self, height: List[int]) -> int:

        trapped_water = 0

        l = 0
        r = len(height) - 1

        maxL = height[l]
        maxR = height[r]

        while l < r:
            
            # left is less than right
            if maxL < maxR:
                l += 1
                water_to_add = maxL - height[l]
                if height[l] > maxL:
                    maxL = height[l]
            # right less than left
            elif maxR < maxL:
                r -= 1
                water_to_add = maxR - height[r]
                if height[r] > maxR:
                    maxR = height[r]
            # pointers are equal (shift left over)
            else:
                l += 1
                water_to_add = maxL - height[l]
                if height[l] > maxL:
                    maxL = height[l]

            if water_to_add > 0:
                trapped_water += water_to_add

        return trapped_water



        
        