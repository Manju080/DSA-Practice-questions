#49.Anagram brute force solution 
#unfortunately not optimal solution

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def dictionary(dic1):
            dic={}
            for i in range(len(dic1)):
                dic[dic1[i]]=1+dic.get(dic1[i],0)
            return dic
        def result(strs):
            arr=[]
            new=[]
            for i in range(len(strs)):
                if strs[i]=="":
                    arr.append(strs[i])
                return new.append(arr)
            i=1
            temp=strs[0]
            while(i<len(strs)):

                if dictionary(temp)==dictionary(strs[i]):
                    arr.append(strs[i])
                    strs.pop(i)
                i+=1    
                if i==len(strs):
                    arr.append(temp)
                    strs.pop(0)
                    temp=strs[0]
                    new.append(arr)
                    arr=[]
                    i=1
            if len(strs)==1:

                arr=[]
                arr.append(strs[0])
                new.append(arr)

            return new
        
        
                
        res=result(strs)
        return res