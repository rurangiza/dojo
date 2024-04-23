# Date: 06/11/2029

"""
Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters
of a different word or phrase, typically using all the
original letters exactly once.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

from collections import defaultdict
from typing import List

class Solution(object):
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            anagrams["".join(sorted(s))].append(s)
        return (values for values in anagrams.values())

#############################################

def main():
    obj = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    groups = obj.groupAnagrams(strs)
    for group in groups:
        print(group)

if __name__ == "__main__":
    main()