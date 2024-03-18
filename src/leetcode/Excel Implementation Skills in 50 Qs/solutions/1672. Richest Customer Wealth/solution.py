class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        result = 0
        for account in accounts:
            current_wealth = sum(account)

            result = max(result, current_wealth)

        return result
        
