#include <stdio.h>

/**
 * IN PROGRESS
 * Note: The returned array must be malloced, assume caller calls free().
 */

int* mergeSort(int* nums, int size) {
    if (size == 1)
        return nums;
    
    mergeSort();
}

int* sortArray(int* nums, int numsSize, int* returnSize) {
    mergeSort(nums, numsSize);
    return NULL;
}

int main() {

    int nums[10] = {34, 23, 6, 88, 2, 56, 89, 3, 45, 100};
    int size = 10;

    int* sorted = sortArray(&nums, size, size);

    return 0;
}