class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sorted_words_index = {}

        for i in range(len(strs)):
            count = [0] * 26

            for ch in strs[i]:
                count[ord(ch) - ord('a')] += 1

            result = []

            for letter in range(26):
                # Loops through 0-25 and addes that to the int representation of 'a' and adds it the amount of times it occurs
                result.append(chr(letter + ord('a')) * count[letter])

            sorted_word = ''.join(result)

            if sorted_word not in sorted_words_index:
                sorted_words_index[sorted_word] = [strs[i]]
            else:
                sorted_words_index[sorted_word].append(strs[i])

        return list(sorted_words_index.values())
