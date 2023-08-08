class Solution {
public:
    int strStr(string haystack, string needle) {
        int haystackLength = haystack.length();
        int needleLength = needle.length();

        // Handle special cases
        if (needleLength == 0) {
            return 0;
        }
        if (haystackLength < needleLength) {
            return -1;
        }
        
        for (int i = 0; i <= haystackLength - needleLength; ++i) {
            int j = 0;
            while (j < needleLength && haystack[i + j] == needle[j]) {
                j++;
            }
            if (j == needleLength) {
                return i;
            }
        }

        return -1;

    }
};
