class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_dict = {}

        for i in nums:
            if i not in freq_dict:
                freq_dict[i] = 1
            else:
                freq_dict[i] += 1

        arr = []

        for pair in freq_dict:
            arr.append([freq_dict[pair],pair])

        arr.sort()

        # print(arr)

        res = []

        for i in range(len(arr) - 1, len(arr) - k-1, -1):
            # print("last k items ",arr[i])
            res.append(arr[i][1])

        return res
        