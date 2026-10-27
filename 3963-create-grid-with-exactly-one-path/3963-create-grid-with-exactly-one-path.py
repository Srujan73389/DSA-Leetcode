class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid=[""]*m
        grid[0]="."*n
        rest="#"*(n-1) + "."
        for i in range(1,m):
            grid[i]=rest
        return grid
        