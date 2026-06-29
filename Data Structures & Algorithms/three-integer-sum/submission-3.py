class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []

        print(nums)

        # At each place this basically turns into two-sum where the target is the number you look for
        for i in range(len(nums)):
            # Here nums[i] is the target that you are trying to reach using everything but nums[i]
            target = 0 - nums[i]

            print(nums[i], i)

            l = i + 1
            r = len(nums) - 1

            while l < r:

                # Checking to add it to 
                if (nums[l] + nums[r]) == target:
                    to_add = [nums[l], nums[i] , nums[r]]
                    to_add.sort()
                    # print(l, i , r, to_add)
                    if to_add not in res:
                        res.append(to_add)
                    l += 1
                    r -= 1

                # moving pointers otherwise
                elif (nums[l] + nums[r]) < target:
                    l += 1
                else:
                    r -= 1

        return res
        