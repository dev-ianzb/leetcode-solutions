# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

# Example 5:

# Input: s = "([)]"

# Output: false

 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.



# My Solution:
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {
        ')': '(',
        ']': '[',
        '}': '{'
        }
        reference = []

        for x in s:
            
            if x in brackets.values():
                reference.append(x)
            elif x in brackets:
                if not reference:
                    return False
                if reference[-1] != brackets[x]:
                    return False
                reference.pop()

        if len(reference) == 0:
            return True
        else: 
            return False