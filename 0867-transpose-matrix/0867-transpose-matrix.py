class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row,col=len(matrix),len(matrix[0])
        output=[[0]*row for i in range(col)]
        for r in range(row):
            for j in range(col):
                output[j][r]=matrix[r][j]
        return output
        