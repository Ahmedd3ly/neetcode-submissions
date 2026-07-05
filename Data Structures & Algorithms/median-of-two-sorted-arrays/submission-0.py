class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = nums1, nums2
        total = len(n1) + len(n2)
        half = total // 2

        if len(n1) > len(n2):
            n1, n2 = nums2, nums1

        l, r = 0, len(n1) - 1

        while True:
            mid1 = (l + r) // 2
            mid2 = half - mid1 - 2

            n1Left  = n1[mid1] if mid1 >= 0 else float('-infinity')
            n1Right = n1[mid1 + 1] if (mid1 + 1) < len(n1) else float('infinity')
            n2Left  = n2[mid2] if mid2 >= 0 else float('-infinity')
            n2Right = n2[mid2 + 1] if (mid2 + 1) < len(n2) else float('infinity')

            # portion is correct
            if n1Left <= n2Right and n2Left <= n1Right:
                # odd?
                if total % 2:
                    return min(n1Right, n2Right)
                # even?
                return (max(n1Left, n2Left) + min(n1Right, n2Right)) / 2
            elif n1Left > n2Right:
                r = mid1 - 1
            else:
                l = mid1 + 1
