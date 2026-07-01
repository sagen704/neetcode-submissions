class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        return self.stack.pop(-1)
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        min_value = self.stack[0]

        for number in self.stack:
            if number < min_value:
                min_value = number
        return min_value
        
