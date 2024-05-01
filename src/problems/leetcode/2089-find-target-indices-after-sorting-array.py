from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        res = []
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                res.append(mid)
                left, right = mid-1, mid+1
                while left >= 0 and nums[left] == target:
                    res.append(left)
                    left -= 1
                while right < len(nums) and nums[right] == target:
                    res.append(right)
                    right += 1
                return sorted(res)
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return res