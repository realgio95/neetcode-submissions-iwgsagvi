class MinStack:

    # ["MinStack", "push", 5, "push", 0, "push", 2, "push", 4, "getMin", "pop", "getMin", "pop", "getMin"]
    # mys 5 0 2 4, pop4, 5 0 2, pop2, 5 0 . 5 0 
    # mins 5 0 0 0, getmin=0, 5 0 getmin=0, getmin=0 
    def __init__(self):
        self.mystack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.mystack.append(val)
        # add to minstack if the current value is less than whats on the minstack currently    
        if self.minstack and val <= self.minstack[-1]:
            self.minstack.append(val)
        elif self.minstack and val > self.minstack[-1]:
            self.minstack.append(self.minstack[-1])
        elif not self.minstack:
            self.minstack.append(val)
        
    def pop(self) -> None:
        self.mystack.pop()
        self.minstack.pop()

    def top(self) -> int:
        top = self.mystack[-1]        
        return top

    def getMin(self) -> int:
        if self.minstack:
            minval = self.minstack[-1]
            return minval 



        
