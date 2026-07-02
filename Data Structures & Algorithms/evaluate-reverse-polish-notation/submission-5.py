class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for token in tokens:
            # print("Adding " , token)

            if token.lstrip('-+').isdigit():
                stack.append(token)
            else:
                # Need evaluation logic here 
                second_number = stack.pop()
                first_number = stack.pop()
                inner_answer = eval(f"{first_number}{token}{second_number}")
                stack.append(str(int(inner_answer)))

        return int(stack.pop())
        