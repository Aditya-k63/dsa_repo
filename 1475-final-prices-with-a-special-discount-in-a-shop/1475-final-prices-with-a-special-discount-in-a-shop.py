class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack=[]
        ans=list(prices)

        for i in range (len(prices)):
            while stack and prices[stack[-1]]>=prices[i]:
                top_idx=stack.pop()

                ans[top_idx]=prices[top_idx] - prices[i]

            stack.append(i)
        return ans