"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity is neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached.
If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range.
Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.



Example 1:
Input: s = "42"
Output: 42

Explanation:
The underlined characters are what is read in and the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
Example 2:
Input: s = " -042"
Output: -42

Explanation:
Step 1: "   -042" (leading whitespace is read and ignored)
            ^
Step 2: "   -042" ('-' is read, so the result should be negative)
             ^
Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
               ^
Example 3:
Input: s = "1337c0d3"
Output: 1337

Explanation:
Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
         ^
Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
             ^
Example 4:
Input: s = "0-1"
Output: 0

Explanation:
Step 1: "0-1" (no characters read because there is no leading whitespace)
         ^
Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)
          ^
Example 5:
Input: s = "words and 987"
Output: 0

Explanation:

Reading stops at the first non-digit character 'w'.

Constraints:

0 <= s.length <= 200
s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.
"""

examples = {
    "42": "42",
    "   -042": "-42",
    "    -88827   5655  U": "-88827",
    "1337c0d3": "1337",
    "0-1": "0",
    "+-12": "0",
    "-5-": "-5",
    "-13+8": "-13",
    "123-": "123",
    "  +  413": "0"
}


class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0 or (len(s) == 1 and not s[0].isdigit()) or len(s.strip()) == 0:
            return 0

        has_digit = False
        result = ""
        has_signal = None
        leading_whitespace = True
        for char in s:
            if char != " ":
                leading_whitespace = False
            if not char.isdigit() and char not in ["-", "+"] and not leading_whitespace:
                if has_digit:
                    break
                else:
                    return 0
            elif not char.isdigit():
                if has_digit:
                    break
                if char in ["-", "+"]:
                    if has_signal and not has_digit:
                        return 0
                    if not has_signal:
                        has_signal = char
            else:
                result += char
                has_digit = True

        if has_signal:
            result = has_signal + result

        result = int(result)
        if result > 2 ** 31:
            return 2 ** 31 + 1
        elif result < (-2 ** 31) - 1:
            return -2 ** 31
        else:
            return result


if __name__ == '__main__':
    for key, value in examples.items():
        result = Solution().myAtoi(key)
        print(result, result == int(value))
