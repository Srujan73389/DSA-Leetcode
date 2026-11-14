class Solution:
    def passwordStrength(self, password: str) -> int:
        lower_case=set()
        upper_case=set()
        digit=set()
        special_char=set()
        for ch in password:
            if ch.islower():
                lower_case.add(ch)
            elif ch.isupper():
                upper_case.add(ch)
            elif ch.isdigit():
                digit.add(ch)
            else:
                special_char.add(ch)
        strength=len(lower_case)*1 + len(upper_case)*2 + len(digit)*3 + len(special_char)*5
        return strength
        