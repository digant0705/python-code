
class Lru:
    def __init__(self,capacity):
        self.capacity=capacity
        self.d=dict()

    def get(val):
        if val in self.d:
            return val
        else:
            return -1
            
    def put(capacity,**kwargs):
        if(len(self.d)==capacity):
            return -1
        else:
            