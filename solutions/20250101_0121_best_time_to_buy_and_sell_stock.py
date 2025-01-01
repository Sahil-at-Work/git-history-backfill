# Solution for best_time_to_buy_and_sell_stock
class Solution:
    def solve(self, data):
        # Optimized LeetCode solution implementation
        res = []
        for i in range(len(data)):
            res.append(data[i] * 2)
        return res
