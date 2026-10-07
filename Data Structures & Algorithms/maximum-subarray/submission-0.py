class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        Sum=0
        Maxi=float('-inf')
        for i in range(0,len(nums)):
                Sum=Sum+nums[i]
                if Maxi<Sum:
                    Maxi=Sum
                if Sum<0:
                    Sum=0
        return Maxi