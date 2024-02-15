class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int size = prices.size();
        if(size == 0) return 0;
        
        int result = 0;
        for(int i = 0; i < size - 1; i++)
        {
            int r = prices[i + 1] - prices[i];
            if(r > 0)
            {
                result += r;     
            }
        }
        
        return result;
    }
};
