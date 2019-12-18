from unittest import TestCase

from problems.longest_palindrome.longest_palindrome import Solution


class TestLongestPalindrome(TestCase):

    def test_babad_is_bab(self):
        # Given
        string = "babad"

        # When
        longest = Solution().longestPalindrome(string)

        # Then
        assert longest == "bab" or longest == "aba"

    def test_cbbd_is_bb(self):
        # Given
        string = "cbbd"

        # When
        longest = Solution().longestPalindrome(string)

        # Then
        assert longest == "bb"

    def test_wqecbbca_is_cbbc(self):
        # Given
        string = "wqecbbca"

        # When
        longest = Solution().longestPalindrome(string)

        # Then
        assert longest == "cbbc"

    def test_a_is_a(self):
        # Given
        string = "a"

        # When
        longest = Solution().longestPalindrome(string)

        # Then
        assert longest == "a"

    def test_bb_is_bb(self):
        # Given
        string = "bb"

        # When
        longest = Solution().longestPalindrome(string)

        # Then
        assert longest == "bb"
