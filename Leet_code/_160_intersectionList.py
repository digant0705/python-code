# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA  or not  headB:
            return
        ha=headA
        hb=headB
        countA=0
        countB=0
        while ha.next:
            ha=ha.next
            countA+=1
            
        while hb.next:
            hb=hb.next
            countB+=1
            
            
        if countA-countB>=0:
            ha=headA
            x=0
            while 1:
                if x==countA-countB:
                    break
                else:
                    ha=ha.next
                x+=1
            hb=headB
           
        else:
            
            hb=headB
            x=0
            while 1:
                if x==countB-countA:
                    break
                else:
                    hb=hb.next
                x+=1
            ha=headA
        while 1:
            
            if hb==ha:
                
                break
            else:
                hb=hb.next
                ha=ha.next
        
             
        return ha
            
            
            
                
                
        
        
            
            
        