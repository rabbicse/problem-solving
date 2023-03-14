class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int> agNums;

        for(int i = 0; i < nums.size(); i++) {
            agNums.push_back(pow(nums[i], 2));
        }

        sort(agNums.begin(), agNums.end());

        return agNums;
    }
};
