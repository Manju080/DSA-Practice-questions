#reversing linked list using lists
#leetcode solution
class Solution:
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    values=[]
    temp=result=head
    while temp:
    values.append(temp.val)
    temp=temp.next
    while head:
    head.val=values.pop()
    head=head.next
return result