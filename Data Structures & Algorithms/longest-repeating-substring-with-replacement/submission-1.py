class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        character_frequencies = {}
        longest_substring = 0

        l = 0

        for r in range(len(s)):

            # Growing the window
            if s[r] not in character_frequencies:
                character_frequencies[s[r]] = 1
            else:
                character_frequencies[s[r]] = character_frequencies[s[r]] + 1

            # Shrinking the window
            while (r - l + 1) - max(character_frequencies.values()) > k:
                character_frequencies[s[l]] = character_frequencies[s[l]] - 1
                l += 1


            # Update the answer
            total = sum(character_frequencies.values())
            print(character_frequencies, longest_substring, total)

            if total > longest_substring:
                longest_substring = total
        
        return longest_substring