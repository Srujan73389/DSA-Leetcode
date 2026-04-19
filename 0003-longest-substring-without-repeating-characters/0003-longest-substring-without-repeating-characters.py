class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=0
        win=set()
        le=0
        for i in range(len(s)):
            while s[i] in win:
                win.remove(s[l])
                l+=1
            win.add(s[i])
            le=max(le,i-l+1)
        return le
        