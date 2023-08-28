class ListNode:
    def __init__(self, val=0, next=None) :
        self.val = val
        self.next = next

def addTwoNumers(l1 : ListNode, l2 : ListNode) -> ListNode :
    head = ListNode(0)
    tracker = head

    carry = 0

    while carry or l1 or l2 :
        if l1 :
            carry += l1.val
            l1 = l1.next

        if l2 : 
            carry += l2.val
            l2 = l2.next

        tracker.next = ListNode(carry % 10)
        carry //= 10
        tracker = tracker.next

    return head.next