from typing import List

###


class CheckDuplicate:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


###
class NearbyKDuplicate:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = dict()

        for index in range(len(nums)):
            if (nums[index] in seen) and (abs(seen[nums[index]] - index) <= k):
                return True
            seen[nums[index]] = index
        return False




# Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
# Output: true
# Explanation: We can choose (i, j) = (0, 3).
# We satisfy the three conditions:
# i != j --> 0 != 3
# abs(i - j) <= indexDiff --> abs(0 - 3) <= 3
# abs(nums[i] - nums[j]) <= valueDiff --> abs(1 - 1) <= 0

# Input: nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
# Output: false
# Explanation: After trying all the possible pairs (i, j), we cannot satisfy the three conditions, so we return false.