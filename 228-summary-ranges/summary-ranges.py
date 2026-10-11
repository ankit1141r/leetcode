class Solution:
    def summaryRanges(self, a: List[int]) -> List[str]:
        n = len(a)
        if n<1:
            return []

        res = []
        # is_start = True
        cur = str(a[0])
    
        for i in range(1, n):
            if a[i] - a[i-1] != 1:
                end = str(a[i-1])

                if end == cur: res.append(cur)
                else: res.append(cur+"->"+end)

                cur = str(a[i])

        if cur != "":
            if cur == str(a[-1]): res.append(cur)
            else: res.append(cur+"->"+str(a[-1]))
                
        return res