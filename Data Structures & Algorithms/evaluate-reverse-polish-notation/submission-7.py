class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for token in tokens:
            # print("Adding " , token)

            if token.lstrip('-+').isdigit():
                stack.append(token)
            else:
                # Need evaluation logic here 
                second_number = int(stack.pop())
                first_number = int(stack.pop())

                if token == '+':
                    stack.append(first_number + second_number)
                elif token == '-':
                    stack.append(first_number - second_number)
                elif token == '*':
                    stack.append(first_number * second_number)
                else:
                    stack.append(first_number / second_number)

        return int(stack.pop())
        