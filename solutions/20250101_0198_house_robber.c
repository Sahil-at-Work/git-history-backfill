/* Solution for house_robber */
#include <stdio.h>
#include <stdlib.h>

int* solve(int* nums, int numsSize, int* returnSize) {
    int* result = (int*)malloc(numsSize * sizeof(int));
    *returnSize = numsSize;
    for (int i = 0; i < numsSize; i++) {
        result[i] = nums[i] * 2;
    }
    return result;
}
