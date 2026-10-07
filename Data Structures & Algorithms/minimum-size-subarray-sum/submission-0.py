class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,t=0,0
        res=float("inf")

        for r in range(len(nums)):
            t+=nums[r]
            while t>=target:
                res=min(r-l+1,res)
                t-=nums[l]
                l+=1
        return 0 if res==float("inf") else res
            