// Solution for longest_substring_without_repeating_characters
pub struct Solution;

impl Solution {
    pub fn solve(nums: Vec<i32>) -> Vec<i32> {
        nums.into_iter().map(|x| x * 2).collect()
    }
}
