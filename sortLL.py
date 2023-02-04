# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        left = head  
        right  = self.splitList(head)

        #print(left,'\n', right)  you can print this code to help understand

        left = self.sortList(head)
        right = self.sortList(right)

        return self.mergeList(left, right)


    def splitList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        fast, slow = head.next, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        middle = slow.next
        slow.next = None

        return middle


    def mergeList(self, left: ListNode, right: ListNode) -> ListNode:
        dummy = head = ListNode()

        while left and right:
            if left.val <= right.val:
                dummy.next = left
                left = left.next
            else:
                dummy.next = right
                right = right.next
            
            dummy = dummy.next
        
        dummy.next = left or right
        
        return head.next
						
						
						
        