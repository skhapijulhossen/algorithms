"""20. Valid Parentheses
Easy
21.4K
1.4K
Companies
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
Accepted
3.6M
Submissions
9M
Acceptance Rate
40.2%"""


def isValid( s: str) -> bool:
    closedMap = {')':'(', ']':'[', '}':'{'}
    stack = []

    for p in s:
        if p in closedMap:
            if stack and stack[-1] == closedMap[p]:
                stack.pop()
            else:
                return False
            continue
        stack.append(p)
    return not stack


s = "()"
print(isValid(s))
s = "()[]{}"
print(isValid(s))
s = "(]"
print(isValid(s))