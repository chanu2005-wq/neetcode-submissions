class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        Mod=10**9+7
        n=len(arr)
        dp=[0]*n
        st,res=[],0
        for i in range(n):
            while st and arr[st[-1]]>arr[i]:
                st.pop()

            j=st[-1] if st else -1
            dp[i]=(dp[j] if j!=-1 else 0)+arr[i]*(i-j)
            dp[i]%=Mod
            res=(res+dp[i])%Mod
            st.append(i)
        return res
