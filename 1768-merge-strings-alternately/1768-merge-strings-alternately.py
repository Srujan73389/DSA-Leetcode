class Solution(object):
    def mergeAlternately(self, word1, word2):
        i=j=0
        res=""
        while i<len(word1) and j<len(word2):
            res+=word1[i]
            res+=word2[j]
            i+=1
            j+=1
        res+=word1[i:]
        res+=word2[j:]
        return res
        

        