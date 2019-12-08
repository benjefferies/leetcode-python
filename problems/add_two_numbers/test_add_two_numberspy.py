from unittest import TestCase

from problems.add_two_numbers.add_two_numbers import ListNode, Solution


class TestAddTwoNumbers(TestCase):

    def test_342_add_465_is_807(self):
        first = ListNode(2)
        first.next = ListNode(4)
        first.next.next = ListNode(3)
        second = ListNode(5)
        second.next = ListNode(6)
        second.next.next = ListNode(4)

        total = Solution().addTwoNumbers(first, second)

        assert total.val == 7
        assert total.next.val == 0
        assert total.next.next.val == 8

    def test_5_add_5_is_0_1(self):
        first = ListNode(5)
        second = ListNode(5)

        total = Solution().addTwoNumbers(first, second)

        assert total.val == 0
        assert total.next.val == 1

    def test_8_and_1_add_0_is_1_8(self):
        first = ListNode(1)
        first.next = ListNode(8)
        second = ListNode(0)

        total = Solution().addTwoNumbers(first, second)

        assert total.val == 1
        assert total.next.val == 8
