class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        boat=0
        start,end=0,len(people)-1
        while start<=end:
            if people[start]+people[end]<=limit:
                start+=1
            end-=1
            boat+=1
            
        return boat
       
        
       
        