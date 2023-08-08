class Solution {
public:
    bool isPalindrome(string s) {        
        // Remove non-alphanumeric characters
        s.erase(std::remove_if(s.begin(), s.end(), [](char c) {
            return !isalnum(c);
        }), s.end());
        
        // Convert string to lowercase
        for (char& c : s) {
            c = tolower(c);
        }

        // Check if the modified string is a palindrome
        int left = 0;
        int right = s.length() - 1;
        while (left < right) {
            if (s[left] != s[right]) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
};
