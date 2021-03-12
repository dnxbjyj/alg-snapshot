# V2
# AC@228ms, 10%, 14%, O(n), O(1)
# 双指针法
from typing import *

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # - 边界判断
        if not height or len(height) < 2:
            return 0

        # - 双指针，从两端到中间，终止条件：i == j；收缩区间条件：收缩高度较低的那一端
        # 思考：如何证明上述算法的正确性？
        size = len(height)
        left = 0
        right = size - 1

        max_area = 0
        while left < right:
            # - 更新最大面积
            left_height = height[left]
            right_height = height[right]
            area = min(left_height, right_height) * (right - left)
            if area > max_area:
                max_area = area

            # 收缩区间，收缩依据：收缩高度较低的那一端
            if left_height < right_height:
                left += 1
            else:
                right -= 1
        return max_area

if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))  # 49
    print(s.maxArea([1,1]))  # 1
    print(s.maxArea([4,3,2,1,4]))  # 16
    print(s.maxArea([1,2,1]))  # 2
