class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre_tot, post_tot = 0, 0
        prefix, postfix = [0] * len(nums), [0] * len(nums)
        for i in range(len(nums)):
            pre_tot += nums[i]
            prefix[i] = pre_tot

            post_tot += nums[(len(nums)-1)-i]
            postfix[len(nums)-1-i] = post_tot
        
        ans = []
        for i in range(0, len(nums)):
            leftSum = prefix[i-1] if i > 0 else 0
            rightSum = postfix[i+1] if i < len(nums)-1 else 0
            ans.append(abs(leftSum - rightSum))
        return ans

nums = [10,4,8,3]
obj = Solution()
ans = obj.leftRightDifference(nums)
print(ans)