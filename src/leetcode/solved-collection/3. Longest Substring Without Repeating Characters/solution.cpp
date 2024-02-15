class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if(s.length() == 0) return 0;

        set<char> chars;
        int ans = 0;
        int n = s.size();
        int i = 0, j = 0;

        while(i < n && j < n) {           
            if(chars.find(s[j]) == chars.end()) {
                chars.insert(s[j]);
                ans = max(ans, j - i + 1);
                j++;
            } else {
                chars.erase(s[i]);
                i++;
            }
        }

        return ans;
    }
};
