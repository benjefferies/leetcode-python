class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        no_repeat_string = ""
        max_count = 0
        for char in s:
            if char in no_repeat_string:
                max_count = max_count if len(no_repeat_string) < max_count else len(no_repeat_string)
                index_repeat = no_repeat_string.index(char)
                no_repeat_string = no_repeat_string[index_repeat + 1:]
                no_repeat_string = no_repeat_string + char
            else:
                no_repeat_string = no_repeat_string + char
        return max_count if len(no_repeat_string) < max_count else len(no_repeat_string)
