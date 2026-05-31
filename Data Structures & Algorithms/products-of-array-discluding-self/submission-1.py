class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = len(nums) * [1]

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    res[i] = res[i] * nums[j]


        return res

        