class Solution(object):
    def reversePairs(self, nums):
        def mS(st, end):
            if st == end:
                return 0
            mid = (st+end)//2
            leftPairs = mS(st, mid)
            rightPairs = mS(mid+1, end)
            pairs = countPairs(st, mid, end)
            merge(st, mid, end)
            return leftPairs + rightPairs + pairs
        def countPairs(st, mid, end):
            count = 0
            j = mid+1
            for i in range(st, mid+1):
                while j<=end and nums[i] > 2 * nums[j]:
                    j+=1
                    
                count += j - (mid + 1)
            return count
        def merge(st, mid, end):
            temp = []
            i, j = st, mid + 1
            while i <= mid and j <= end:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            while i <= mid:
                temp.append(nums[i])
                i += 1
            while j <= end:
                temp.append(nums[j])
                j += 1
            nums[st:end+1] = temp

        return mS(0, len(nums) - 1)