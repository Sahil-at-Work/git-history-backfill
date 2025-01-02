// Solution for longest_increasing_subsequence
public class Solution {
    public int[] solve(int[] nums) {
        int[] result = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            result[i] = nums[i] * 2;
        }
        return result;
    }
}
