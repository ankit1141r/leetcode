class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans=[]
        nums1,nums2=sorted(nums1),sorted(nums2)
        one,two=0,0
        while one<len(nums1) and two<len(nums2):
            if nums1[one]==nums2[two]:
                ans.append(nums1[one])
                one+=1
                two+=1
            elif nums1[one]<nums2[two]:
                one+=1
            elif nums1[one]>nums2[two]:
                two+=1       
        return ans