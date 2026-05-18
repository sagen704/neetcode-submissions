class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        '''
        So first I created a dictionary for the frequency of how many times you see each number
        I sorted the values of the the dictionaries and saved them to a list frequencies
        Then from this I loop through k times to get the most frequent elements from the value of its frequency
        '''

        num_count = {}
        elements = [0] * k

        for num in nums:
            if num not in num_count:
                num_count[num] = 1
            else:
                num_count[num] += 1

        freqs = list(num_count.values())

        freqs.sort(reverse=True)

        for i in range(k):
            for number in num_count:
                if num_count[number] == freqs[i] and number not in elements:
                    elements[i] = number

        return elements


        