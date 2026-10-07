class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # iterative
        nums.sort()
        subsets = [[]]
        for i in range(len(nums)):
            si = ei if i > 0 and nums[i] == nums[i-1] else 0
            ei = len(subsets)
            for j in range(si, ei):
                subsets.append(subsets[j] + [nums[i]])
        return subsets

