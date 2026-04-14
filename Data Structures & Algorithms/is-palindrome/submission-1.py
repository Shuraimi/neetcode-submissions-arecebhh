class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=''
        for char in s:
            if char.isalnum():
                st+=char.lower()
        rev_st=st[::-1]
        if rev_st==st:
            return True
        else:
            return False