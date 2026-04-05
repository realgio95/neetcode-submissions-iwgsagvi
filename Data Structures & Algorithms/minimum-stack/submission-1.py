class MinStack:

    def __init__(self):
        self.mystack = []
        self.prefixStack = []
        

    def push(self, val: int) -> None:
        self.mystack.append(val)

    def pop(self) -> None:
        if self.mystack:
            self.mystack.pop()

    def top(self) -> int:
        top = self.mystack[-1]        
        return top

    def getMin(self) -> int:
        if not self.mystack:
            minval = float('inf')
            return minval
        else:
            minval = float('inf')
            for num in self.mystack:
                if num < minval:
                    minval = num
        return minval        
        

        
