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

#Merge Two Linked List 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() 
        tail = dummy 

        while list1 and list2: 
            if list1.val < list2.val: 
                tail.next = list1  
                list1 = list1.next 
            else: 
                tail.next =list2
                list2 = list2.next 
            tail = tail.next 

        #fill in the rest of the linkedlist 
        if list1: 
            tail.next = list1 
        if list2: 
            tail.next = list2 
        
        return dummy.next 
        
