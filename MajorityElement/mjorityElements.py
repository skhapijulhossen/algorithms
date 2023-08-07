"""229. Majority Element II
Medium
7.9K
354
Companies
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]
 

Constraints:

1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109
 

Follow up: Could you solve the problem in linear time and in O(1) space?"""


from typing import List


def majorityElement(nums: List[int]) -> int:
    # Optimal Solution - Moore's voting for 2 elements Time: O(n) Space: O(1)
    candidate1, candidate2 = 0, 0
    vote1, vote2 = 0, 0

    length = len(nums)
    # getting top 2 frequent elements
    for index in range(length):
        if vote1 == 0 and nums[index] != candidate2:
            vote1 = 1
            candidate1 = nums[index]
        elif vote2 == 0 and nums[index] != candidate1:
            vote2 = 1
            candidate2 = nums[index]
        elif nums[index] == candidate1:
            vote1 += 1
        elif nums[index] == candidate2:
            vote2 += 1
        else:
            vote1 -= 1
            vote2 -= 1
    # validating counts >= N/3
    vote1, vote2 = 0, 0
    for index in range(length):
        if nums[index] == candidate1:
            vote1 += 1
            continue
        if nums[index] == candidate2:
            vote2 += 1
            continue

    majority = []
    if vote1 > (length//3):
        majority.append(candidate1)
    if vote2 > (length//3):
        majority.append(candidate2)
    return majority



nums = [3,2,3]
print(majorityElement(nums))

nums = [1]
print(majorityElement(nums))

nums = [1,2]
print(majorityElement(nums))