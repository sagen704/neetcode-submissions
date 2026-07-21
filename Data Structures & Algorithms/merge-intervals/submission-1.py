class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        res = []
        intervals.sort()
        print(intervals)

        l = 0

        for i in range(1, len(intervals)):
            if intervals[l][1] >= intervals[i][0]:
                
                intervals[l][1] = intervals[i][1] if intervals[i][1] > intervals[l][1] else intervals[l][1]
            else:
                res.append(intervals[l])
                l = i

        res.append(intervals[l])

        return res
        