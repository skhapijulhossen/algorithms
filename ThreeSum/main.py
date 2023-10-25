"""
15. 3Sum
Medium
28.9K
2.6K
Companies
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""


def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    out = []
    nums.sort()

    for idx, num in enumerate(nums):
        if num > 0:
            break
        if idx > 0 and num == nums[idx-1]:
            continue  # to skip duplicates

        left, right = idx + 1, len(nums) - 1
        while left < right:
            summ = num + nums[left] + nums[right]

            if summ > 0:
                right -= 1
            elif summ < 0:
                left -= 1
            else:
                out.append([num, nums[left], nums[right]])
                left += 1
                right -= 1

                while nums[left] == nums[left-1] and left < right:
                    left += 1
    return out


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    print(threeSum(nums))
    nums = [0, 1, 1]
    print(threeSum(nums))
    nums = [0, 0, 0]
    print(threeSum(nums))
