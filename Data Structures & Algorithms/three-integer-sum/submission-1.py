class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []

        # At each place this basically turns into two-sum where the target is the number you look for
        for i in range(len(nums)):
            # Here nums[i] is the target that you are trying to reach using everything but nums[i]
            target = 0 - nums[i]

            l = 0
            r = len(nums) - 1

            while l < r:

                # this is making sure you only have one of each of the indexes
                if l == i:
                    l += 1
                elif r == i:
                    r -= 1

                # Checking to add it to 
                elif (nums[l] + nums[r]) == target:
                    to_add = [nums[l], nums[i] , nums[r]]
                    to_add.sort()
                    # print(l, i , r, to_add)
                    res.append(to_add) if to_add not in res else None
                    l += 1
                    r -= 1
                # moving pointers
                elif (nums[l] + nums[r]) < target:
                    l += 1
                else:
                    r -= 1

        return res
        