class Solution(object):
    def groupAnagrams(self, strs):
        grouped={}
        for word in strs:
            sort=''.join(sorted(word))
            if sort in grouped:
                grouped[sort].append(word)
            else:
                grouped[sort]=[word]
        return list(grouped.values())
        
        
        