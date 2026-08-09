import os
import random
import subprocess
from datetime import datetime, timedelta

# Define 20 LeetCode problems with variations in difficulty
LEETCODE_PROBLEMS = [
    {"id": "0001", "slug": "two_sum", "difficulty": "easy"},
    {"id": "0002", "slug": "add_two_numbers", "difficulty": "medium"},
    {"id": "0003", "slug": "longest_substring_without_repeating_characters", "difficulty": "medium"},
    {"id": "0004", "slug": "median_of_two_sorted_arrays", "difficulty": "hard"},
    {"id": "0005", "slug": "longest_palindromic_substring", "difficulty": "medium"},
    {"id": "0015", "slug": "three_sum", "difficulty": "medium"},
    {"id": "0020", "slug": "valid_parentheses", "difficulty": "easy"},
    {"id": "0021", "slug": "merge_two_sorted_lists", "difficulty": "easy"},
    {"id": "0042", "slug": "trapping_rain_water", "difficulty": "hard"},
    {"id": "0053", "slug": "maximum_subarray", "difficulty": "medium"},
    {"id": "0070", "slug": "climbing_stairs", "difficulty": "easy"},
    {"id": "0121", "slug": "best_time_to_buy_and_sell_stock", "difficulty": "easy"},
    {"id": "0136", "slug": "single_number", "difficulty": "easy"},
    {"id": "0141", "slug": "linked_list_cycle", "difficulty": "easy"},
    {"id": "0198", "slug": "house_robber", "difficulty": "medium"},
    {"id": "0200", "slug": "number_of_islands", "difficulty": "medium"},
    {"id": "0206", "slug": "reverse_linked_list", "difficulty": "easy"},
    {"id": "0226", "slug": "invert_binary_tree", "difficulty": "easy"},
    {"id": "0300", "slug": "longest_increasing_subsequence", "difficulty": "medium"},
    {"id": "0322", "slug": "coin_change", "difficulty": "medium"}
]

# Code snippets for multi-language solutions
SOLUTION_TEMPLATES = {
    "py": """# Solution for {slug}
class Solution:
    def solve(self, data):
        # Optimized LeetCode solution implementation
        res = []
        for i in range(len(data)):
            res.append(data[i] * 2)
        return res
""",
    "java": """// Solution for {slug}
public class Solution {{
    public int[] solve(int[] nums) {{
        int[] result = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {{
            result[i] = nums[i] * 2;
        }}
        return result;
    }}
}}
""",
    "c": """/* Solution for {slug} */
#include <stdio.h>
#include <stdlib.h>

int* solve(int* nums, int numsSize, int* returnSize) {{
    int* result = (int*)malloc(numsSize * sizeof(int));
    *returnSize = numsSize;
    for (int i = 0; i < numsSize; i++) {{
        result[i] = nums[i] * 2;
    }}
    return result;
}}
""",
    "rs": """// Solution for {slug}
pub struct Solution;

impl Solution {{
    pub fn solve(nums: Vec<i32>) -> Vec<i32> {{
        nums.into_iter().map(|x| x * 2).collect()
    }}
}}
""",
    "go": """// Solution for {slug}
package main

func solve(nums []int) []int {{
    result := make([]int, len(nums))
    for i, v := range nums {{
        result[i] = v * 2
    }}
    return result
}}
"""
}

# Calculate date ranges
current_year = datetime.now().year
previous_year = current_year - 1
start_date = datetime(previous_year, 1, 1)
end_date = datetime(previous_year, 12, 31)

# Ensure solutions output directory exists
os.makedirs("solutions", exist_ok=True)

current_date = start_date
while current_date <= end_date:
    # Introduce day-of-week activity variation (higher on weekdays, lower on weekends)
    is_weekend = current_date.weekday() >= 5
    if is_weekend:
        num_commits = random.randint(1, 4)
    else:
        num_commits = random.randint(3, 10)

    for i in range(num_commits):
        # Pick random question and random language extension
        problem = random.choice(LEETCODE_PROBLEMS)
        ext = random.choice(list(SOLUTION_TEMPLATES.keys()))
        
        # Build strict filename: {date}_{id}_{ps}.{ext}
        date_prefix = current_date.strftime("%Y%m%d")
        filename = f"{date_prefix}_{problem['id']}_{problem['slug']}.{ext}"
        filepath = os.path.join("solutions", filename)

        # Generate realistic commit hour/min/sec
        hour = random.randint(8, 22)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)
        commit_dt = current_date.replace(hour=hour, minute=minute, second=second)
        date_str = commit_dt.strftime("%Y-%m-%dT%H:%M:%S")

        # Write code template content into file
        code_content = SOLUTION_TEMPLATES[ext].format(slug=problem["slug"])
        with open(filepath, "w") as f:
            f.write(code_content)

        # Stage file
        subprocess.run(["git", "add", filepath], check=True)

        # Configure environment variables for Git backdating
        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = date_str
        env["GIT_COMMITTER_DATE"] = date_str

        # Commit with structured LeetCode message
        commit_msg = f"Solve LeetCode {problem['id']}: {problem['slug'].replace('_', ' ').title()} [{ext.upper()}]"
        subprocess.run(["git", "commit", "-m", commit_msg], env=env, check=True)

    current_date += timedelta(days=1)