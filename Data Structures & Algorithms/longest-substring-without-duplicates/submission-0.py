class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        right = 0

        my_set = set()
        while right < len(s):
            if s[right] not in my_set:
                my_set.add(s[right])
                longest = max(longest, len(my_set))
                right += 1
            else:
                my_set.remove(s[left])
                left += 1
        return longest