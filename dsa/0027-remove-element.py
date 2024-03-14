# Date: 01/11/2023

"""
Given an integer array nums and an integer val,
remove all occurrences of val in nums in-place.
The order of the elements may be changed.
Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k,
to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums
contain the elements which are not equal to val.
The remaining elements of nums are not important as well as the size of nums.

Return k.
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        p1 = 0
        for p2 in range(len(nums)):
            if nums[p2] != val:
                nums[p1] = nums[p2]
                p1 += 1
        return p1

#############################################

def main():
    obj = Solution()
    nums = [1, 2, 3, 3, 3, 4, 5, 3, 6]
    val = 3
    length = obj.removeElement(nums, val)
    print(f"len: {length} | {nums[:length]}")

if __name__ == "__main__":
    main()