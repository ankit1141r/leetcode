# class Solution:
#     def myAtoi(self, s: str) -> int:
#         symbol,count=1,0
#         num=0
#         minimum=-2**31
#         maximum=2**31-1
#         for i in range(len(s)):
#             if s[i]==" " and num==0 and count==0:
#                 continue
#             elif (s[i]=="+" or s[i]=="-") and num==0 and count==0 :
#                 count+=1
#                 if s[i]=="-":
#                     symbol=-1
#                 if count>1:
#                     break
#                 if not s[i+1].isdigit():
#                     break
#             elif s[i].isdigit():
#                 num = num * 10 + int(s[i])
#                 if symbol*num<minimum:
#                     return minimum      
#                 elif symbol*num>maximum:
#                     return maximum        
#             else:
#                 break
#         return num*symbol
class Solution(object):
    def myAtoi(self, s):
        n = len(s)
        i=0
        # skip leading zeroes
        while i<n and s[i]==' ':
            i+=1
        # check sign
        sign = 1
        if i<n and s[i]=='-':
            sign = -1
            i+=1
        elif i<n and s[i]=='+':
            i+=1
        # build number
        num =0
        while i<n and s[i].isdigit():
            d = int(s[i])
            num =num*10+d
            i+=1
        num*=sign
        # bring in range
        intMin = -2**31
        intMax = 2**31 - 1
        if num< intMin:
            return intMin
        if num>intMax:
            return intMax
        return num
              
                    
