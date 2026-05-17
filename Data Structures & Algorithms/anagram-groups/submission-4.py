class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        '''
        First I create a dictionary with the word_hash : List of words that are the annagram

        loop through all the word turn it into a hashed tuple of that word to save time on reconstruction

        then I check if that hash is in the dict and if it is create a list of the words of that anagram
        '''
        sorted_words_index = {}

        for i in range(len(strs)):
            count = [0] * 26

            for ch in strs[i]:
                count[ord(ch) - ord('a')] += 1

            word_hashed = tuple(count)

            if word_hashed not in sorted_words_index:
                sorted_words_index[word_hashed] = [strs[i]]
            else:
                sorted_words_index[word_hashed].append(strs[i])

        return list(sorted_words_index.values())
