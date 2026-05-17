class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
            
        letters_dict = {}

        for letter in s:
            if letter not in letters_dict:
                letters_dict[letter] = 1
            else:
                letters_dict[letter] += 1
        for letter in t:
            if letter not in letters_dict:
                return False
            else:
                letters_dict[letter] -= 1
        
        print(letters_dict)
        
        return len(set(letters_dict.values())) == 1
        