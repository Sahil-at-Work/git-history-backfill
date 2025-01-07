# Solution for linked_list_cycle
class Solution:
    def solve(self, data):
        # Optimized LeetCode solution implementation
        res = []
        for i in range(len(data)):
            res.append(data[i] * 2)
        return res
