from unittest import TestCase

from problems.median_two_sorted_lists.median_two_sorted_lists import Solution


class TestMedianTwoSortedLists(TestCase):

    def test_1_3_list_and_2_list_is_2(self):
        # Given
        nums1 = [1, 3]
        nums2 = [2]

        # When
        median = Solution().findMedianSortedArrays(nums1, nums2)

        # Then
        assert median == 2

    def test_1_2_list_and_3_4_list_is_2_5(self):
        # Given
        nums1 = [1, 2]
        nums2 = [3, 4]

        # When
        median = Solution().findMedianSortedArrays(nums1, nums2)

        # Then
        assert median == 2.5

    def test_empty_list_and_2_3_list_is_2_5(self):
        # Given
        nums1 = []
        nums2 = [2, 3]

        # When
        median = Solution().findMedianSortedArrays(nums1, nums2)

        # Then
        assert median == 2.5

