// Solution for three_sum
package main

func solve(nums []int) []int {
    result := make([]int, len(nums))
    for i, v := range nums {
        result[i] = v * 2
    }
    return result
}
