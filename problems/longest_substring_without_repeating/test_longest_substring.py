import unittest

from problems.longest_substring_without_repeating.longest_substring import Solution


class TestLongestSubstring(unittest.TestCase):

    def test_abcabcbb_should_be_3_abc(self):
        # Given
        string = "abcabcbb"

        # When
        length = Solution().lengthOfLongestSubstring(string)

        # Then
        assert length == 3

    def test_bbbbb_should_be_1_b(self):
        # Given
        string = "bbbbb"

        # When
        length = Solution().lengthOfLongestSubstring(string)

        # Then
        assert length == 1

    def test_pwwkew_should_be_3_wke(self):
        # Given
        string = "pwwkew"

        # When
        length = Solution().lengthOfLongestSubstring(string)

        # Then
        assert length == 3

    def test_space_should_be_1(self):
        # Given
        string = " "

        # When
        length = Solution().lengthOfLongestSubstring(string)

        # Then
        assert length == 1

    def test_aab_should_be_2(self):
        # Given
        string = "aab"

        # When
        length = Solution().lengthOfLongestSubstring(string)

        # Then
        assert length == 2

    def test_dvdf_should_be_3(self):
        # Given
        string = "dvdf"

        # When
        length = Solution().lengthOfLongestSubstring(string)

        # Then
        assert length == 3
