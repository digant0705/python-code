arr=[2,7,4,1,8,1,1]
def f(l):
    while(len(l)>1 ):
        
        l.sort()
        print("sorted array--",l)

        if l[-1]==l[-2]:
            l=l[:len(l)-2]
            print(l)
    
        else:
            x=abs(l[-1]-l[-2])
            l=l[:len(l)-2]
            l.append(x)
            print(l)

    if len(l):

        return l[0]
    else:
        return 0

print(f(arr))

"""
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[-stone for stone in stones]
        heapq.heapify(heap)
        while(len(heap)>1):
            
            x=heapq.heappop(heap)
            y=heapq.heappop(heap)
            
            if x!=y:
                heapq.heappush(heap,-abs(x-y))
        
        if len(heap)>0:
            return -heap[0]
        else:
            return 0
        """