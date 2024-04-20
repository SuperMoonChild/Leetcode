#Since Singly-linked list did not have double pointers, therefore, they not direct reverse the linked list problem 
#So we have to assign two head notes, None and next 
#Assign the next node to curr.next 
#point the curr node reversed back to the prev node 
#move two pointers, prev = curr, curr = nect node 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev,curr = None,head 

        while curr: 
            next = curr.next
            curr.next = prev 
            prev = curr 
            curr = next 
        return prev 
