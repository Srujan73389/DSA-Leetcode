class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        a,b=0,1
        ans=[]
        if n==0 or n==1:
            return n
        else:
            for i in range(n+1):
                ans.append(a)
                a,b=b,a+b
            return ans[n]
        