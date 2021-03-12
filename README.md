# alg-snapshot
算法快照，以版本迭代思想从0到1迭代优化解决各种算法问题。

# 问题目录
## [leetcode-cn](https://github.com/dnxbjyj/alg-snapshot/tree/master/leetcode-cn)
### [lc11-盛最多水的容器](https://github.com/dnxbjyj/alg-snapshot/tree/master/leetcode-cn/lc11_container-with-most-water)
- 版本数：2
- 版本路线图：暴力算法（O(n^2)） > 双指针算法（O(n)）
- 当前最优算法核心思想：双指针，以较低高度的一端为收缩区间的依据，以left==right为终止条件。

### [lc42-接雨水](https://github.com/dnxbjyj/alg-snapshot/tree/master/leetcode-cn/lc42_trapping-rain-water)
- 版本数：2
- 版本路线图：暴力算法（O(n^2)） > 使用最大高度前缀/后缀数组备忘录优化算法（O(n)）
- 当前最优算法核心思想：每次聚焦当前柱子课贡献容量，使用最大高度前缀/后缀数组备忘录时间复杂度。

