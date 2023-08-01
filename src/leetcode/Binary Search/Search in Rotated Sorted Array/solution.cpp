class Solution {
public:
    int search(vector<int>& nums, int target) {
        unordered_map <int, int> map;
        for(int i = 0; i < nums.size(); i++) {
            map[nums[i]] = i;
        }
        sort(nums.begin(), nums.end());        
        
        int start = 0;
        int end = nums.size() - 1;
        
        while(start <= end) {
            int mid = start + (end - start) / 2;
            cout << mid << endl;
            if(nums[mid] == target) return map[nums[mid]];
            else if(target < nums[mid]) {
                end = mid - 1;
            } else if(target > nums[mid]) {
                start = mid + 1;
            }
        }
        return -1;
    }
};
