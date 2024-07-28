"""
Longest Substring Without Repeating Characters

Given a string s, find the length of the longest
substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

given_responses = {
    "abcabcbb": 3,
    "bbbbb": 1,
    "pwwkew": 3,
    "au": 2,
    "": 0,
    " ": 1,
    "dvdf": 3,
}


class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        var = set()
        max_len = 0
        left = 0
        for right in range(len(s)):
            if s[right] not in var:
                var.add(s[right])
                max_len = len(var) if len(var) > max_len else max_len
            else:
                while s[right] in var:
                    var.remove(s[left])
                    left += 1
                var.add(s[right])
        return len(var) if len(var) > max_len else max_len


if __name__ == '__main__':
    for key, value in given_responses.items():
        result = Solution().length_of_longest_substring(key)
        print(result, result == value)
