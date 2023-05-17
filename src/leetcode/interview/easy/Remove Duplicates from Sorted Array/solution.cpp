class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int size = nums.size();
        
        int ans = 1;
        for(int i = 1; i < size; i++) {
            if(nums[i - 1] != nums[i]) {
                nums[ans] = nums[i];
                ans++;
            }
        }
        
        return ans;
    }
};
