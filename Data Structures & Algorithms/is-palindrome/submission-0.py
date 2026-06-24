class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned_string = [character.lower() for character in s if character.isalnum()]

        l = 0
        r = len(cleaned_string) - 1

        # print(cleaned_string)

        for i in range(len(cleaned_string)//2):
            # print(cleaned_string[l + i] , cleaned_string[r - i])
            if cleaned_string[l + i] != cleaned_string[r - i]:
                return False

        return True