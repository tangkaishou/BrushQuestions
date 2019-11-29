"""
示例 1：

输入：arr = [4,2,1,3]
输出：[[1,2],[2,3],[3,4]]
示例 2：

输入：arr = [1,3,6,10,15]
输出：[[1,3]]
示例 3：

输入：arr = [3,8,-10,23,19,-4,-14,27]
输出：[[-14,-10],[19,23],[23,27]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-absolute-difference
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        result = []
        min_num = arr[1] - arr[0] # 记录最小的差值
        for i in range(len(arr) - 1):
            num = arr[i+1] - arr[i]
            if min_num == num:
                result.append([arr[i],arr[i+1]])
            elif min_num > num:
                result.clear()
                result.append([arr[i], arr[i+1]])
                min_num = num
        return result
