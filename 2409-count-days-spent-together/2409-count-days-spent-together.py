class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        pref=[0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        def convert_to_num(date):
            month,day=int(date[:2]),int(date[3:])
            return pref[month-1]+day
        start=max(convert_to_num(arriveAlice),convert_to_num(arriveBob))
        end=min(convert_to_num(leaveAlice),convert_to_num(leaveBob))
        return max(0,end-start+1)
        