# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1,l2 = headA, headB
        while l1 != l2:         #either are gonna be the same(intersection) or they are both going to be null (no intersection)
            l1 = l1.next if l1 else headB   # if l1.next == None, we move to the starting of the other linked list
            l2 = l2.next if l2 else headA   # if l2.next == None, we move to the starting of the first linked list
        return l1



        
        