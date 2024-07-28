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

        max_string = ""
        for i in range(n - 1):
            for j in range(n):
                if s[i:j + 1] == s[i:j + 1][::-1]:
                    max_string = s[i:j + 1] if len(s[i:j + 1]) > len(max_string) else max_string

        return max_string


if __name__ == '__main__':
    for key, value in responses.items():
        result = Solution.longest_palindrome(key)
        print(result, result == value)
