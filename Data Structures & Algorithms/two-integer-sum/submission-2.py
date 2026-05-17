class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_required_first_index_dict = {}

        for i in range(len(nums)):

            number_required_to_hit_sum = target - nums[i]

            if nums[i] in num_required_first_index_dict:
                return [num_required_first_index_dict[nums[i]],i]
            else:
                num_required_first_index_dict[number_required_to_hit_sum] = i

