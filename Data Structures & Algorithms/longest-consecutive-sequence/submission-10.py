class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = set(nums)

        if len(nums) == 0:
            return 0

        numbers_dict = {}

        # convert to dictionary
        for number in nums:
            numbers_dict[number] = None

        # print(numbers_dict)

        starting_numbers = {}

        # get starting numbers
        for number in numbers_dict:
            if number - 1 not in numbers_dict:
                # print(f"this is the start of a sequence: {number}")
                starting_numbers[number] = 0

        # looping from starting number to len(array)
        for number in starting_numbers:
            for i in range(number, number+len(nums) + 1):
                if i in numbers_dict:
                    # print(f"in sequence: {i}")
                    starting_numbers[number] = starting_numbers[number] + 1
                else:
                    break
            # print()

        # print(starting_numbers)
        return max(starting_numbers.values())
            