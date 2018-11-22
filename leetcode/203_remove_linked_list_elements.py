# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return head
        dummy = ListNode(1)
        dummy.next = head
        last = dummy
        current = head
        while current != None and current.next != None:
            if current.val == val:
                while current != None and (current.val == val):
                    current = current.next
                last.next = current
            else:
                if current.next == None and (current.val == val): 
                    last.next = None
                else:
                    last = current
                current = current.next
        if current != None and current.val == val: last.next = None
        return dummy.next

