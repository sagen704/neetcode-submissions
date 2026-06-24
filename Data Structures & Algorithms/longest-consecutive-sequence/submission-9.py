class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = set(nums)

        total_max = 0

        for number in nums:
            local_max = 0

            if number - 1 not in nums:
                next_number = 0

                while number + next_number in nums:
                    local_max += 1
                    if local_max >= total_max:
                        total_max = local_max
                    next_number += 1
        
        return total_max
            