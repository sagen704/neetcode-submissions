class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sDict = {}
        tDict = {}

        if len(s) != len(t):
            return False
        for i in s:
            if i not in sDict:
                sDict[i] = 0
            else:
                sDict[i] += 1
        for i in t:
            if i not in tDict:
                tDict[i] = 0
            else:
                tDict[i] += 1

        return sDict == tDict