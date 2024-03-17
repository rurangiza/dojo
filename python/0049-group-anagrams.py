# Date: 06/11/2029

"""
Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters
of a different word or phrase, typically using all the
original letters exactly once.
"""

from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams_map = defaultdict(list)
        groups = []

        for s in strs:
            anagrams_map[tuple(sorted(s))].append(s)
        for key, values in anagrams_map.items():
            groups.append(values)
        return groups

#############################################

def main():
    obj = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    groups = obj.groupAnagrams(strs)
    for group in groups:
        print(group)

if __name__ == "__main__":
    main()