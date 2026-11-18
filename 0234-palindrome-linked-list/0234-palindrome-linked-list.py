# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        list2 =slow
        prev=None
        while list2:
            next_node=list2.next
            list2.next=prev
            prev=list2
            list2=next_node
        j =prev
        i =head
        while j:
            if i.val!=j.val:
                return False
            i=i.next
            j=j.next
        return True