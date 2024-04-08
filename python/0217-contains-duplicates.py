"""
Given an integer array nums, return true if any value appears at least twice
in the array, and return false if every element is distinct.
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        myDict = defaultdict()

        for num in nums: # O(n)
            if num in myDict:
                return True
            else:
                myDict[num] = 1
        return False