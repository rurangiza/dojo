

"""
Solve a probleme
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c in "[({":
                stack.append(c)
            else:
                tmp = stack[-1]
                print(f"on stack == {tmp}")
                print(f"c == {c}")
                stack.pop()
                if c == "]" and tmp != "[":
                    print("hereee")
                    return False
                elif c == ")" and tmp != "(":
                    print("hereee")
                    return False
                elif c == "}" and tmp != "{":
                    print("hereee")
                    return False
        return True

obj = Solution()
res = obj.isValid("()")
print(res)