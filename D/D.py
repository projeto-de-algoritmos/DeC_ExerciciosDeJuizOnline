class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ans = []
        i, j, k = 0, 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                ans.append(nums1[i])
                k += 1
                i += 1
            else:
                ans.append(nums2[j])
                k += 1
                j += 1

        while i < len(nums1):
            ans.append(nums1[i])
            k += 1
            i += 1

        while j < len(nums2):
            ans.append(nums2[j])
            k += 1
            j += 1

        n = k
        median = 0.0

        if n % 2 == 1:
            median = ans[n // 2]
        else:
            median = (ans[n // 2 - 1] + ans[n // 2]) / 2.0

        return median