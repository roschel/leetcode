"""
Example 1:

Input: num = 3749

Output: "MMMDCCXLIX"

Explanation:

3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC as 500 (D) + 100 (C) + 100 (C)
  40 = XL as 10 (X) less of 50 (L)
   9 = IX as 1 (I) less of 10 (X)
Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places

###################################
Example 2:

Input: num = 58

Output: "LVIII"

Explanation:

50 = L
8 = VIII

##################################3
Example 3:

Input: num = 1994

Output: "MCMXCIV"

Explanation:

1000 = M
 900 = CM
  90 = XC
   4 = IV


Constraints:

1 <= num <= 3999
"""

examples = {
    3749: "MMMDCCXLIX",
    58: "LVIII",
    1994: "MCMXCIV"
}


class Solution:
    def intToRoman(self, num: int) -> str:
        num_map = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }
        result = ""
        for n in reversed(num_map.keys()):
            while n <= num:
                result += num_map[n]
                num -= n
        return result


if __name__ == '__main__':
    for input, result in examples.items():
        x = Solution().intToRoman(input)
        print(result, x == result)
