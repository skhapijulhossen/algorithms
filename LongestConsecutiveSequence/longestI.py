"""128. Longest Consecutive Sequence
Medium
17.5K
766
Companies
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9"""

from typing import List


def longestConsecutive(nums: List[int]) -> int:
    numsSet = set(nums)

    maxx = 0
    for idx in range(len(nums)):

        if not (nums[idx] - 1) in numsSet:
            count = 1
            while (nums[idx] + count) in numsSet:
                count += 1
            maxx = max(count, maxx)
    return maxx


nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(nums))

nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(longestConsecutive(nums))
