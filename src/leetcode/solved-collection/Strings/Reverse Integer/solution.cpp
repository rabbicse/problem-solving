class Solution {
public:
    int reverse(int x) {
        string text = to_string(x);
               
        int i = 0;
        int n = text.size() - 1;
        
        while(i < n) {     
            if(text[i] == '-') {
                i++;
                continue;
            }
            char temp = text[i];
            text[i] = text[n];
            text[n] = temp;            
            
            i++;
            n--;
        }
        
        
        long long result = stoll(text);
        
        // Check for integer overflow/underflow
        if (result > INT_MAX || result < INT_MIN) {
            return 0;
        }
        
        return static_cast<int>(result);
    }
};
