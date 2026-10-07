class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
           # Always binary search on the smaller array
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        m, n = len(nums1), len(nums2)
        lo, hi = 0, m

        while lo <= hi:
            # partition1: # of elements from nums1 in the left half
            partition1 = lo + (hi - lo) // 2
            # partition2: remaining elements needed for left half
            partition2 = (m + n + 1) // 2 - partition1

            # Edge values: use -INF/+INF when partition is at array boundary
            L1 = nums1[partition1 - 1] if partition1 > 0 else float('-inf')
            R1 = nums1[partition1]     if partition1 < m else float('inf')
            L2 = nums2[partition2 - 1] if partition2 > 0 else float('-inf')
            R2 = nums2[partition2]     if partition2 < n else float('inf')

            if L1 <= R2 and L2 <= R1:
                # ✅ Valid partition found
                if (m + n) % 2 == 1:
                    return max(L1, L2)                          # Odd total
                else:
                    return (max(L1, L2) + min(R1, R2)) / 2.0   # Even total

            elif L1 > R2:
                hi = partition1 - 1   # nums1's left side too large → move left
            else:
                lo = partition1 + 1   # nums1's left side too small → move right

        raise ValueError("Input arrays are not sorted")