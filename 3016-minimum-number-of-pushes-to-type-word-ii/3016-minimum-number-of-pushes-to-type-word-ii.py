class Solution:
    def minimumPushes(self, word: str) -> int:
        freq={}

        for i in range(len(word)):
            if word[i] in freq:
                freq[word[i]]+=1
            else:
                freq[word[i]]=1
        freqency=list(freq.values())
        freqency.sort(reverse=True)
        ans=0
        for i in range(len(freqency)):
            pushes=(i//8)+1
            ans+=pushes*freqency[i]
        return ans
        