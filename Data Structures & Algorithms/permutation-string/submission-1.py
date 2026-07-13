class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1_counts = {chr(i + ord('a')) : 0 for i in range(26)}
        s2_counts = {chr(i + ord('a')) : 0 for i in range(26)}

        for i in range(len(s1)):
            s1_counts[s1[i]] += 1
            s2_counts[s2[i]] += 1

        matches = 0

        for i in range(26):
            letter = chr(i + ord('a'))
            if s1_counts[letter] == s2_counts[letter]:
                matches += 1

        # Sliding window portion

        l = 0

        for r in range(len(s1), len(s2)):

            if matches == 26: return True

            # update the count at right pointer
            k = s2[r]
            s2_counts[k] += 1
            if s1_counts[k] == s2_counts[k]:
                matches += 1
            elif s1_counts[k] + 1 == s2_counts[k]:
                matches -= 1

            # update the count at the left pointer
            lk = s2[l]
            s2_counts[lk] -= 1
            if s1_counts[lk] == s2_counts[lk]:
                matches += 1
            elif s1_counts[lk] - 1 == s2_counts[lk]:
                matches -= 1
            l += 1

        return matches == 26