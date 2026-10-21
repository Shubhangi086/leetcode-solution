class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans={}
        for c in s:
            ans[c]=ans.get(c,0)+1
        for i in range(len(s)):
            if ans[s[i]]==1:
                return i
        return -1
