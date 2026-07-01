class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        parentheses_dict = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for parentheses in s:
            if parentheses == "{" or parentheses == "(" or parentheses == "[":
                stack.append(parentheses)
            else:
                if stack:
                    checking_parentheses = stack.pop(-1)
                    if parentheses_dict[parentheses] != checking_parentheses:
                        return False
                else:
                    return False
        
        return True if not stack else False


        