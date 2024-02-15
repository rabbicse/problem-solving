func maxProfit(prices []int) int {
    if len(prices) == 0 {
        return 0
    }
    
    ans := 0
    
    for i := 0; i < len(prices) - 1; i++ {
        result := prices[i + 1] - prices[i]
        
        if result > 0 {
            ans += result
        }
    }
    
    return ans
}
