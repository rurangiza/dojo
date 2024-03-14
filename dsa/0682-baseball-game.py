# Date: 02/11/2023

"""
You are keeping the scores for a baseball game with strange rules.
At the beginning of the game, you start with an empty record.

You are given a list of strings operations,
where operations[i] is the ith operation you must apply
to the record and is one of the following:

An integer x: Record a new score of x.
'+': record a new score that is the sum of the previous two scores.
'D' : record a new score that is the double of the previous score.
'C' : invalidate the previous score, removing it from the record.

Return the sum of all the scores on the record after applying all the operations.
"""

class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack , total = [], 0
        for op in operations:
            try:
                num = int(op)
                stack.append(num)
            except ValueError:
                if op == "+":
                    stack.append(stack[-2] + stack[-1])
                elif op == "D":
                    stack.append(stack[-1]*2)
                elif op == "C":
                    stack.pop()
        for num in stack:
            total += num
        return total
    
        """
        Notes: used the try to check if it's a number
        while accepting signs (+-). Because str.isdigit()
        does not accept signs
        
        Could've checked; if op.strip(-+).isdigit()

        + list is emptu
        + adding when less then 2 numbers
        """
        
#############################################

def main():
    obj = Solution()
    operations = ["5","-2","4","C","D","9","+","+"]
    res = obj.calPoints(operations)
    print(res)


if __name__ == "__main__":
    main()