class MinStack:

    def __init__(self):
        
        self.stack=[]
        self.y=0
        """
        initialize your data structure here.
        """
        

    def push(self, x: int) -> None:
        if self.stack ==[]:
            self.stack.append(x)
            self.y=x
        
        else:    
            self.stack.append(x)
            if x<self.y:
                self.y=x
        

    def pop(self) -> None:
        if len(self.stack)>0:
            self.stack.pop()
            m=float("inf")
            for i in self.stack:
                m=min(m,i)
            self.y=m
        

    def top(self) -> int:
        if len(self.stack)>0:
            return self.stack[-1]
        else:
            return None
        

    def getMin(self) -> int:
        if len(self.stack)>0:
            return self.y
        else:
            return -float("inf")
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(6)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3,param_4)