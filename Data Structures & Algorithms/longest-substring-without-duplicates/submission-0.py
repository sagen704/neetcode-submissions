class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        in_window_dict = {}
        max_length = 0

        left = 0

        for right in range(len(s)):
            letter_checking = s[right]
            print(s[left:right])

            # Grow Window
            if s[right] not in in_window_dict:
                in_window_dict[s[right]] = None
                max_length = right + 1 - left if right + 1 - left > max_length else max_length

            # Shrink Window
            else:
                while letter_checking in in_window_dict:
                    in_window_dict.pop(s[left])
                    left += 1
                in_window_dict[s[right]] = None

        return max_length
        