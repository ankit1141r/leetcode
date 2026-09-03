class Solution:
    def reverseWords(self, s: str) -> str:
        n=len(s)
        i=0
        while s[i]==" ":
            s.replace(" ","",1)
            i+=1
        s=s[::-1]
        while s[i]==" ":
            s.replace(" ","",1)
            i+=1
        s=" ".join([word[::-1] for word in s.split()])

        return s    
                
                