def maxProfit(self, prices: List[int]) -> int:
        prices=[1,2,3,4,5]
        m=0
        dp=[0]*(len(prices)+2)
        dp[len(prices)]=0
        dp[len(prices)+1]=0
        dp[0]=0
        l=1
        for i in reversed(prices): 
            k=0
            for j in range(len(prices)-l,len(prices)): 
                k=max(prices[j]-i,prices[j]-i + dp[j+1])   
                m=max(k,m)
            dp[len(prices)+1-l]=m
            l+=1
        return m
        
        """class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        last_price=float("inf")
        profit=0
        
        for price in prices:
            if price>last_price:
                profit=profit+price-last_price
            last_price=price
        
        return profit
        
        """
