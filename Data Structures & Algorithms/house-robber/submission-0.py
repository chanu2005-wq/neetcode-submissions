class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1=0
        prev2=0
        n=len(nums)
        for i in range(n):
            temp=prev1
            prev1=max(nums[i]+prev2,prev1)
            prev2=temp
        return prev1