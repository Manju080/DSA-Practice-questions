class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        right=1
        maxprofit=0
        arr=[]
        while(right<len(prices)):
            profit=prices[right]-prices[left]
            if prices[left]<prices[right]:
                maxprofit=max(profit,maxprofit)
                left+=1
                arr.append(profit)
            else:
                left=right
            right+=1
        return sum(arr)