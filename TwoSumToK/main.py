from typing import List, Tuple

"""
167. Two Sum II - Input Array Is Sorted
Medium
10.9K
1.3K
Companies
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 

Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
"""


def get_two_sum_k(arr: List[int], k: int) -> Tuple:
    """
    ### Time: O(n)    Space: O(2*n)
    """
    if len(arr) < 2 or k < 0:
        return -1

    start, end = 0, len(arr)
    summ = arr[start]
    mapSpace = {}

    while start < end:
        required = k - arr[start]
        found = mapSpace.get(required, None)
        if found:
            return start, found
        mapSpace[arr[start]] = start
        start += 1
    return -1, -1


def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    left, right = 0, len(numbers) - 1

    while left < right:
        summ = numbers[left] + numbers[right]
        if summ < target:
            left += 1
        elif summ > target:
            right -= 1
        else:
            return [left+1, right+1]


if __name__ == '__main__':
    # array = (1,1,2,3,1,4,2,1)     k=7
    # out = 4
    # array = (1,1,2,3,1,4,2,1)     k=4
    # out = 3
    # array = (4, 2, 3, 2, 1, 2)    k=5
    # out = 3
    # array = (4, 2, 3, 2, 1, 2)    k=8
    # out = 3
    arrays = [
        ((1, 1, 2, 3, 1, 4, 2, 1), 7), ((1, 1, 2, 3, 1, 4, 2, 1), 4),
        ((4, 2, 3, 2, 1, 2), 5), ((4, 2, 3, 2, 1, 2), 8)
    ]
    # Test
    for arr, k in arrays:
        found = get_two_sum_k(arr, k)
        print(f'array={arr} & k={k}:{found}')

    ######
    numbers = [2, 7, 11, 15]
    target = 9
    print(twoSum(numbers=numbers, target=target))
    numbers = [2, 3, 4]
    target = 6
    print(twoSum(numbers=numbers, target=target))
    numbers = [-1, 0]
    target = -1
    print(twoSum(numbers=numbers, target=target))