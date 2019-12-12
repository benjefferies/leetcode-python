# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def _init_uneven_arrays(l1, l2):
    if l1.next is None and l2.next is not None:
        l1.next = ListNode(0)
    if l2.next is None and l1.next is not None:
        l2.next = ListNode(0)


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        _init_uneven_arrays(l1, l2)

        num = l1.val + l2.val
        carry = num % 10

        if l1.next is None or l2.next is None:
            if num - carry >= 10:
                l1.next = ListNode(1)
                l2.next = ListNode(0)
                node = self.addTwoNumbers(l1.next, l2.next)
                new = ListNode(carry)
                new.next = node
                return new
            return ListNode(carry)

        if num - carry >= 10:
            l1.next.val = l1.next.val + 1
        node = self.addTwoNumbers(l1.next, l2.next)
        new = ListNode(carry)
        new.next = node
        return new
