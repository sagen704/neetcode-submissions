class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        print(f"Target = {target}, original right {r}")

        while l <= r:
            m = (r + l) // 2

            print(nums[l:r+1], nums[l], nums[m], nums[r])

            if nums[m] == target:
                return m
            elif nums[l] <= nums[m]: # the left side is sorted:
                if nums[l] <= target < nums[m]:
                    r = m-1
                else:
                    l = m+1
            else: # the right side is sorted
                if nums[m] < target <= nums[r]:
                    l = m+1
                else:
                    r = m-1

        return -1
        