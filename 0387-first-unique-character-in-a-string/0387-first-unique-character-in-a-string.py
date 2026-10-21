class Solution:
    def firstUniqChar(self, s: str) -> int:
        n=len(s)
        for i in range(n):
            count=0
            for k in range(0,i):
                if s[i]==s[k]:
                    count=1
                    break
            if count==0:
                for j in range(i+1,n):
                    if s[i]==s[j]:
                        count=1
                        break
            if count ==0:
                return i
        return -1