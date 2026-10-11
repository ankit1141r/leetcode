class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans=set()
        nums1,nums2=sorted(nums1),sorted(nums2)
        one,two=0,0
        while one<len(nums1) and two<len(nums2):
            if nums1[one]==nums2[two]:
                ans.add(nums1[one])
                one+=1
                two+=1
            elif nums1[one]<nums2[two]:
                one+=1
            elif nums1[one]>nums2[two]:
                two+=1
        ans1=list(ans)
        return ans1

