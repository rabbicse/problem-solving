class Solution {
public:
    int mySqrt(int x) {
        if(x == 0) return x;
        
        int start = 1;
        int end = x;
        
        int mid = x / 2;
        while(start <= end) {
            int mid = start + (end - start) / 2;
            if(mid == x / mid) {
                return mid;
            } else if(mid > x / mid ) {
                end = mid - 1;
            } else if (mid < x / mid) {
                start = mid + 1;
            }
        }
        
        return end;
    }
};
