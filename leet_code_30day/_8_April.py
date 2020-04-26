class ListNode:
    def __init__(self,x):
        self.next=None
        self.value=x

def middleNode(self, head: ListNode) -> ListNode:
    if head is None:
        return -1
    p1=head
    p2=head
      
    while True:
        if p2.next==None:
            return p1`
        if p2.next.next==None:
            return p1.next
        p1=p1.next
        p2=p2.next.next


    