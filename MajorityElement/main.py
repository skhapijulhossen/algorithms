"""169. Majority Element
Easy
16.1K
466
Companies
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

Follow-up: Could you solve the problem in linear time and in O(1) space?
Accepted
1.9M
Submissions
3M
Acceptance Rate
63.9%"""

from typing import List


def majorityElement(nums: List[int]) -> int:
    # Optimal Solution - Moore's voting law Time: O(n) Space: O(1)
    element = None
    vote = 0

    length = len(nums)
    for index in range(length):
        if vote == 0:
            vote = 1
            element = nums[index]
        elif nums[index] == element:
            vote += 1
        else:
            vote -= 1
        
    return element


nums1 = [3,2,3]
nums2 = [2,2,1,1,1,2,2]
print(majorityElement(nums1))
print(majorityElement(nums2))