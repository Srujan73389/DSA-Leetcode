class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        if (x1>xCenter):
            xn=x1
        elif (x2<xCenter):
            xn=x2
        else:
            xn=xCenter
        if (y1>yCenter):
            yn=y1
        elif (y2<yCenter):
            yn=y2
        else:
            yn=yCenter
        return ((xn-xCenter)**2 + (yn-yCenter)**2)<=radius**2
        