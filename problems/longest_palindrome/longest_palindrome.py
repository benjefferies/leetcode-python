class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Return if string is empty
        if not s: return s

        longest_palindrome = ""
        string_length = len(s)
        for index in range(string_length):
            next_character_index = index + 1
            while next_character_not_at_end_of_string(next_character_index, string_length) and \
                    can_be_longer_than_longest_palindrome(s, longest_palindrome, index):
                substring = s[index:next_character_index]
                if is_palindrome(substring) and len(substring) > len(longest_palindrome):
                    longest_palindrome = substring
                next_character_index += 1

        return longest_palindrome


def next_character_not_at_end_of_string(next_character_index, string_length):
    return next_character_index <= string_length


def can_be_longer_than_longest_palindrome(s, longest_palindrome, index):
    return len(longest_palindrome) <= len(s[index:])


def is_palindrome(substring):
    return substring == substring[::-1]
