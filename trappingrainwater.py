#leetcode solution using Greedy algo
res=0
maxlen=0
left=0
right=len(height)-1
while left<right:
    currval =min(height[left],height[right])
    maxlen=max(maxlen,currval)
    if height[left]>height[right]:
        res=res+max(0,maxlen-height[right])
        right-=1
    else:
        res=res+max(0,maxlen-height[left])
        left+=1
return res