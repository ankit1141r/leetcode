class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        matrix =  [""]*numRows
        currRow = 0
        dir = -1
        for ch in s:
            matrix[currRow] += ch
            if currRow == 0 or currRow== numRows-1:
                dir*=-1      
            currRow +=dir    
        return "".join(matrix)