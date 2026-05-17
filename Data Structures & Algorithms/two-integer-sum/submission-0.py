class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumDict = {}
        for i in range(len(nums)):
            if nums[i] in sumDict:
                return [sumDict[nums[i]], i]
            else:
                numNeeded = target - nums[i]
                sumDict[numNeeded] = i


        