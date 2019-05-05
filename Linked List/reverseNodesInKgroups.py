# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def reverseNodesInKGroups(l, k):
    curr = l
    head = ListNode(0)
    it = head
    while curr:
        i = 0
        prev, nxt = None, None
        
        checker = curr
        while checker and i < k:
            checker = checker.next
            i += 1
        if i < k:
            it.next = curr
            break
        
        i = 0
        while curr and i < k:
            i += 1
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
                
        it.next = prev
        while it.next:
            it = it.next
    
    return head.next