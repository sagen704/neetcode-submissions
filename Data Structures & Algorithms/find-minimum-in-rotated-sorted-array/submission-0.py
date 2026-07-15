class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        l = 0
        r = len(nums) - 1

        while l + 1 < r:

            m = (l + r) // 2
            # print(nums[l:r + 1], nums[l], nums[m], nums[r], "Left = ", l, "Right = ", r)

            if (nums[m] < nums[l]) and (nums[m] < nums[r]):
                r = m
            elif (nums[m] > nums[l]) and (nums[m] > nums[r]):
                l = m
            else:
                # its just regular sorted array so wouldnt you just want to take the left
                r = m - 1
                
        return min(nums[l:r+1])