class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s=sum(nums)
        if s%2==1:
            return False
        target=s//2
        n=len(nums)
        dp=[[False]*(target+1) for i in range(n+1)]
        for i in range(n+1):
            dp[i][0]=True
        if nums[0]<=target:
            dp[1][nums[0]]=True
        for i in range(1,n+1):
            for j in range(1,target+1):
                dp[i][j]=dp[i-1][j]
                if j>=nums[i-1]:
                    dp[i][j]=dp[i][j] or dp[i-1][j-nums[i-1]]
        return dp[n][target]