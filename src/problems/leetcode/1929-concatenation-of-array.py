# Date: 02/11/2023

"""
Given an integer array nums of length n,
you want to create an array ans of length 2n
where ans[i] == nums[i] and ans[i + n] == nums[i]
for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.
Return the array ans.
"""

class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [0] * (n*2)
        for i in range(n):
            ans[i], ans[n+i] = nums[i], nums[i]
        return ans
        
#############################################

def main():
    obj = Solution()
    nums1 = [1, 2, 3, 4, 5, 6]
    nums2 = obj.getConcatenation(nums1)
    print(nums1)
    print(nums2)

if __name__ == "__main__":
    main()
    