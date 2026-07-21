class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped={}
        for word in strs:
            sort_word=''.join(sorted(word))
            if sort_word in grouped:
                grouped[sort_word].append(word)
            else:
                grouped[sort_word]=[word]
        return list(grouped.values())

        