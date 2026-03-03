class Solution(object):
    def groupAnagrams(self, strs):
        grouped={}
        for i in strs:
            sorte=''.join(sorted(i))
            if sorte in grouped:
                grouped[sorte].append(i)
                
            else:
                grouped[sorte]=[i]
        return list(grouped.values())
      
        