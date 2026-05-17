class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letters_ana_dict = {}

        for i in strs:
            letters = "".join(sorted(i))
            
            if letters not in letters_ana_dict:
                letters_ana_dict[letters] = [i]
            else:
                letters_ana_dict[letters].append(i)
        
        return list(letters_ana_dict.values())
            
        