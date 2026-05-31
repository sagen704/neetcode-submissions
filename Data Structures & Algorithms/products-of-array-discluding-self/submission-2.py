class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = len(nums) * [1]
        left = len(nums) * [1]
        right = len(nums) * [1]

        for i in range(len(nums)):
            if i != 0:
                left[i] = nums[i-1] * left[i-1]

        for i in range(len(nums)-1, -1, -1):
            if i != len(nums)-1:
                right[i] = nums[i+1] * right[i+1]

        for i in range(len(res)):
            res[i] = left[i] * right[i]
            
        return res

        