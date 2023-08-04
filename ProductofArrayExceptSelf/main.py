"""
238. Product of Array Except Self
Medium
19K
1.1K
Companies
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

Accepted
1.8M
Submissions
2.7M
Acceptance Rate
65.1%
"""
from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    # to store output products
    length = len(nums)
    answer = [1] * length

    # compute prefix product and stores in answer
    pre = 1
    for idx in range(length):
        answer[idx] = pre
        pre = pre * nums[idx]

    # compute prefix product * postfix product and updates answer
    post = 1
    for idx in range(length - 1, -1, -1):
        answer[idx] = post * answer[idx]
        post = post * nums[idx]

    return answer


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    # Output: [24,12,8,6]
    print(productExceptSelf(nums=nums))

    nums = [-1, 1, 0, -3, 3]
    # Output: [0,0,9,0,0]
    print(productExceptSelf(nums=nums))
