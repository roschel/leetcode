"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside
the signed 32-bit integer range [-2^31, (2^31) - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21


Constraints:

-2^31 <= x <= (2^31) - 1
"""


class Solution:
    def reverse(self, x: int) -> int:

        int_str = str(x)
        if "-" in int_str:
            signal = int_str[0]
            reversal = int_str.split("-")[1][::-1]
            reversal = signal + reversal
        else:
            reversal = int_str[::-1]

        if (-2 ** 31) <= int(reversal) <= (2 ** 31) - 1:
            return int(reversal)
        else:
            return 0


if __name__ == '__main__':
    result = Solution().reverse(1534236469)
    print(result, result == -321)
