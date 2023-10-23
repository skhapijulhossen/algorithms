"""
125. Valid Palindrome
Easy
8.4K
8K
Companies
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""

def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    rev = ''
    for c in s:
        rev += c
    if rev == s:
        return True
    return False

if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    print(isPalindrome(s))

    s = "race a car"
    print(isPalindrome(s))
