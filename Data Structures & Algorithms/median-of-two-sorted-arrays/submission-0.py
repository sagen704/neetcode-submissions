class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        total = len(nums1) + len(nums2)
        half = total // 2

        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A

        l = 0
        r = len(A) - 1

        while True:
            m = (r + l) // 2
            j = half - m - 2

            A_left = A[m] if (m) >= 0 else float("-inf")
            A_right = A[m + 1] if (m+1) <= len(A) - 1 else float("inf")
            B_left = B[j] if (j) >= 0 else float("-inf")
            B_right = B[j + 1] if (j+1) <= len(B) - 1 else float("inf")

            if A_left <= B_right and B_left <= A_right:
                if total % 2:
                    return min(A_right, B_right)
                return (max(A_left, B_left) + min(A_right, B_right)) / 2
            elif A_left > B_right:
                r = m - 1
            else:
                l = m + 1
            