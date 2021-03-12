# V1：暴力解法，O(n^2)
# NAC@50/60, TIMEOUT, O(n^2)
from typing import *

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # - 边界判断
        if not height or len(height) == 0:
            return 0

        # - O(n^2)暴力
        size = len(height)
        max_area = 0
        for i in range(size):
            for j in range(i + 1, size):
                cur_area = min(height[i], height[j]) * (j - i)
                if cur_area > max_area:
                    max_area = cur_area
        return max_area

if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))  # 49
    print(s.maxArea([1,1]))  # 1
    print(s.maxArea([4,3,2,1,4]))  # 16
    print(s.maxArea([1,2,1]))  # 2
