# Date: 03/11/2023

"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c in "([{":
                stack.append(c)
            elif c in "})]":
                if not stack:
                    return False
                if c == "}" and stack[-1] != "{":
                    return False
                elif c == "]" and stack[-1] != "[":
                    return False
                elif c == ")" and stack[-1] != "(":
                    return False
                stack.pop()
        if stack:
            return False
        return True
    
# Time complexity = O(n) : since I have to traverse the string
# Space complexity = O(n/2) : since I store all opening characters, so half

#############################################

def main():
    obj = Solution()
    exemple = ""
    print(f"Valid? {obj.isValid(exemple)}")

if __name__ == "__main__":
    main()