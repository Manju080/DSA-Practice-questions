#leetcode solutions
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count=0
        for char in words:
            n=len(char)
            ind=-1
            i=0
            for x in range(len(char)):
                c=char[x]
                ind=ind+1
                while ind<len(s):
                    if c==s[ind]:
                        ind=ind
                        i+=1
                        break
                    ind+=1
            if n==i:
                count+=1
        return(count)