from typing import List

examples = {
    49: [1, 8, 6, 2, 5, 4, 8, 3, 7],
    1: [1, 1]
}


class Solution:
    def maxArea(self, height: List[int]) -> int:
        pass


if __name__ == '__main__':
    for value, height in examples.items():
        result = Solution().maxArea(height)
        print(result, result == value)
