class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            for char in s:
                char_t=t.find(char)
                if char_t!=-1:
                    t=t[:char_t]+t[char_t+1:]
        if t == '':
            return True
        else:
            return False