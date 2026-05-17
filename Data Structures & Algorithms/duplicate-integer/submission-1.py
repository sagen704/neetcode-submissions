class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numDict = {}
        for i in nums:
            if i in numDict:
                return True
            else:
                numDict[i] = None
        return False
         