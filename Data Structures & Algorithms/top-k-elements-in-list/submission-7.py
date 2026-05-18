class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_count = {}
        elements = [0] * k

        for num in nums:
            if num not in num_count:
                num_count[num] = 1
            else:
                num_count[num] += 1

        freqs = list(num_count.values())

        freqs.sort(reverse=True)

        print(freqs)
        print(num_count)

        for i in range(k):
            for number in num_count:
                if num_count[number] == freqs[i] and number not in elements:
                    elements[i] = number

        return elements


        