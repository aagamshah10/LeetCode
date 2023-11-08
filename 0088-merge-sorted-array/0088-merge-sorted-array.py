class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        a=0
        for i in range(len(nums1)):
            if nums1[i]==0:
                nums1[i]=nums2[a]
                a+=1
            if a>=n:
                break
        return nums1.sort()