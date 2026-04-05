# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # used dummy and iterator, if l1 < l2 val, set c next to the l1, else set to l2, 
        # and update next pointer of iterator each loop, including when one list empty just curr.next = l1 eg

        curr = ListNode()
        head = curr

        while (list1 and list2):
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else: 
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        # l1 is not emptu and l2 empty
        if list1 and not list2:
            curr.next = list1
        else:
            curr.next = list2

        return head.next 

















        # iterator = ListNode()
        # dummy = iterator

        # while list1 and list2:
        #     if list1.val < list2.val:
        #         iterator.next = list1
        #         list1 = list1.next 
        #     else:
        #         iterator.next = list2
        #         list2 = list2.next 
        #     iterator = iterator.next

        # iterator.next = list1 if list1 else list2

        # return dummy.next
        # while list1 and list2:
        #     if list1.val < luse a dummy tist2.val:
        #         c.next = list1
        #         list1 = list1.next
        #     else:
        #         c.next = list2
        #         list2 = list2.next
        #     c = c.next
        
        # c.next = list1 if list1 and not list2 else list2

        # return h.next