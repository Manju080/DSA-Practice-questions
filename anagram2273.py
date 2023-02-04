#leetcode 2273
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def dictionary(char):
            dic={}
            for i in range(len(char)):
                dic[char[i]]=1+dic.get(char[i],0)
            return dic
        
        def result(words):
            i=1
            temp=words[0]
            while(i<len(words)):
                if dictionary(temp)==dictionary(words[i]):
                    words.pop(i)
                else:
                    temp=words[i]
                    i+=1
                if i==len(words):
                    return words
            return words
        res=result(words)
        return res