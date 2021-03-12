# version: V3
# AC@48ms, 63%, 12%, O(n), O(n)
# 暴力算法优化：备忘录优化（前/后缀最大值数组）
from typing import *

class Solution:
    '''
    返回一个数组，res[i]表示height[0...i-1]区间的最大高度值
    '''
    def build_left_max_arr(self, height: List[int]) -> List[int]:
        size = len(height)
        res = [0 for i in range(size)]
        left_max = height[0]
        for i in range(0, size):
            res[i] = left_max
            cur = height[i]
            if cur > left_max:
                left_max = cur
        return res
        
    '''
    返回一个数组，res[i]表示height[i+1...size-1]区间的最大高度值
    '''
    def build_right_max_arr(self, height: List[int]) -> List[int]:
        size = len(height)
        res = [0 for i in range(size)]
        res[size - 1] = 0
        right_max = height[size - 1]
        for i in range(size - 1, -1, -1):
            res[i] = right_max
            cur = height[i]
            if cur > right_max:
                right_max = cur
        return res
    
    def trap(self, height: List[int]) -> int:
        # - 边界判断
        if not height or len(height) == 0:
            return 0

        # - 备忘录优化
        size = len(height)
        # [核心思想] 局部贡献思想：height[i]柱子可局部贡献的容量为：res = min(max(height[0...i-1]), max(height[i+1...size-1])) - height[i]，注意：如果左、右最大高度都小于或等于当前高度，则当前柱子是无法贡献容量的。特别的，当i=0时认为左边的height[-1]为0；当i=size-1时认为右边的height[size]为0。所有柱子可容纳的总容量为：sum(res0, res1,..., resN), 其中N = size - 1

        # 总容量
        res = 0
        # 左右最大值数组
        left_max_arr = self.build_left_max_arr(height)
        right_max_arr = self.build_right_max_arr(height)
        for i in range(size):
            # 当前高度
            cur_height = height[i]
            if i == 0 or i == size - 1:
                # 左边最大值（认为是heigth[-1]）为0，所以当前柱子可贡献的容量为0；或者：右边最大值（认为是heigth[size]）为0，所以当前柱子可贡献的容量为0
                continue
            else:
                # 左右两边最大高度中较小的那一个
                lower_height = min(left_max_arr[i], right_max_arr[i])
                # 左、右最大高度至少有一个大于当前高度，才能让当前柱子贡献容量
                if lower_height > cur_height:
                    res = res + (lower_height - cur_height)
        return res
                
if __name__ == '__main__':
    s = Solution()
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
