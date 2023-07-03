"""
347. Top K Frequent Elements
Medium
15K
531
Companies
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

from typing import List


class TopKFrequent:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}    # HashMap to count frequencies
        buckets = [[] for i in range(len(nums) + 1)]    # creating buckets

        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1

        for num, count in freqMap.items():
            # putting numbers having same bucket/count
            buckets[count].append(num)

        out = []
        for bucketIdx in range(len(buckets) - 1, -1, -1):
            for num in buckets[bucketIdx]:
                out.append(num)
                if len(out) == k:   # return when K frequesnt elements found
                    return out
        return out
