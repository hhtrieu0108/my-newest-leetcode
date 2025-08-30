from typing import List, Dict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # My solution
        list_idx: List[int] = []

        for idx1, first_num in enumerate(nums):
            for idx2, second_num in enumerate(nums):
                if idx1 == idx2:
                    continue
                if first_num + second_num == target:
                    list_idx.extend([idx1, idx2])
                    return list_idx
        return []

        ## Best Solution in LeetCode
        # numMap: Dict[int, int] = {}
        # n: int = len(nums)

        # for i in range(n):
        #     complement = target - nums[i]
        #     if complement in numMap:
        #         return [numMap[complement], i]
        #     numMap[nums[i]] = i

        # return []  # No solution found
