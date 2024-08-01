"""
Given a string s, return the longest
palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
"""

responses = {
    "babad": "bab",
    "cbbd": "bb",
    "ac": "a"
}


class Solution:
    @classmethod
    def longest_palindrome(cls, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s

        def expand_from_center(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        max_str = s[0]

        for i in range(n - 1):
            odd = expand_from_center(i, i)
            even = expand_from_center(i, i + 1)

            if len(odd) > len(max_str):
                max_str = odd
            if len(even) > len(max_str):
                max_str = even

        return max_str


if __name__ == '__main__':
    for key, value in responses.items():
        result = Solution.longest_palindrome(key)
        print(result, result == value)
